import json
import os
import time
from datetime import datetime
import threading
import traceback
from TextToSpeach.Fast_DF_TTS import speak
import subprocess
import psutil
import sys
from Features.conversation import ConversationHandler
import inspect

class SelfLearningSystem:
    def __init__(self):
        self.learning_data_path = "Data/learning_data.json"
        self.error_log_path = "Data/error_log.json"
        self.command_history_path = "Data/command_history.json"
        self.recovery_attempts = {}
        self.max_recovery_attempts = 3
        self.feature_data_path = "Data/learned_features.json"
        self.load_data()
        self.start_monitoring()
        self.load_feature_data()

    def load_data(self):
        """Load existing learning data"""
        try:
            if os.path.exists(self.learning_data_path):
                with open(self.learning_data_path, 'r') as f:
                    self.learning_data = json.load(f)
            else:
                self.learning_data = {
                    "command_patterns": {},
                    "error_solutions": {},
                    "successful_commands": [],
                    "failed_commands": [],
                    "last_update": str(datetime.now())
                }
                self.save_data()
        except Exception as e:
            print(f"Error loading learning data: {e}")
            self.learning_data = {}

    def save_data(self):
        """Save learning data"""
        try:
            with open(self.learning_data_path, 'w') as f:
                json.dump(self.learning_data, f, indent=4)
        except Exception as e:
            print(f"Error saving learning data: {e}")

    def log_command(self, command, success=True, error=None):
        """Log command execution for learning"""
        try:
            timestamp = str(datetime.now())
            if success:
                self.learning_data["successful_commands"].append({
                    "command": command,
                    "timestamp": timestamp
                })
            else:
                self.learning_data["failed_commands"].append({
                    "command": command,
                    "error": str(error),
                    "timestamp": timestamp
                })
            self.analyze_command_pattern(command, success)
            self.save_data()
        except Exception as e:
            print(f"Error logging command: {e}")

    def analyze_command_pattern(self, command, success):
        """Analyze command patterns for learning"""
        try:
            words = command.lower().split()
            for i in range(len(words)-1):
                pattern = f"{words[i]} {words[i+1]}"
                if pattern not in self.learning_data["command_patterns"]:
                    self.learning_data["command_patterns"][pattern] = {
                        "success_count": 0,
                        "fail_count": 0
                    }
                if success:
                    self.learning_data["command_patterns"][pattern]["success_count"] += 1
                else:
                    self.learning_data["command_patterns"][pattern]["fail_count"] += 1
        except Exception as e:
            print(f"Error analyzing command pattern: {e}")

    def log_error(self, error, context=None):
        """Log errors and attempt recovery"""
        try:
            # First attempt recovery
            if self.attempt_recovery(error, context):
                speak("Recovery attempt successful")
                return True
                
            # If recovery failed, log the error
            timestamp = str(datetime.now())
            error_data = {
                "error": str(error),
                "traceback": traceback.format_exc(),
                "context": context,
                "timestamp": timestamp,
                "recovery_attempts": self.recovery_attempts.get(str(error), 0)
            }
            
            error_key = str(error)[:100]
            if error_key not in self.learning_data["error_solutions"]:
                self.learning_data["error_solutions"][error_key] = {
                    "occurrences": [],
                    "potential_solutions": []
                }
            
            self.learning_data["error_solutions"][error_key]["occurrences"].append(error_data)
            self.save_data()
            
            # Analyze for patterns
            self.analyze_error(error_key)
            return False
            
        except Exception as e:
            print(f"Error in error logging: {e}")
            return False

    def analyze_error(self, error_key):
        """Analyze errors and try to find solutions"""
        try:
            error_data = self.learning_data["error_solutions"][error_key]
            occurrences = error_data["occurrences"]
            
            if len(occurrences) > 1:
                # Look for patterns in errors
                contexts = [o.get("context", {}) for o in occurrences]
                self.find_error_patterns(error_key, contexts)
        except Exception as e:
            print(f"Error analyzing error: {e}")

    def find_error_patterns(self, error_key, contexts):
        """Find patterns in errors to suggest solutions"""
        try:
            # Basic pattern recognition
            common_elements = {}
            for context in contexts:
                for key, value in context.items():
                    if key not in common_elements:
                        common_elements[key] = []
                    common_elements[key].append(value)
            
            # If we find consistent patterns, suggest solutions
            solutions = []
            for key, values in common_elements.items():
                if len(set(values)) == 1:  # If all values are the same
                    solutions.append(f"Check {key}: always {values[0]}")
            
            if solutions:
                self.learning_data["error_solutions"][error_key]["potential_solutions"] = solutions
                self.save_data()
        except Exception as e:
            print(f"Error finding error patterns: {e}")

    def start_monitoring(self):
        """Start background monitoring"""
        def monitor():
            while True:
                try:
                    # Analyze command patterns periodically
                    self.optimize_command_patterns()
                    # Clean up old data
                    self.cleanup_old_data()
                    time.sleep(3600)  # Check every hour
                except Exception as e:
                    print(f"Error in monitoring: {e}")
                    time.sleep(60)

        threading.Thread(target=monitor, daemon=True).start()

    def optimize_command_patterns(self):
        """Optimize command patterns based on success rates"""
        try:
            for pattern, data in self.learning_data["command_patterns"].items():
                total = data["success_count"] + data["fail_count"]
                if total > 10:  # Only consider patterns with enough data
                    success_rate = data["success_count"] / total
                    if success_rate < 0.3:  # If pattern usually fails
                        print(f"Warning: Command pattern '{pattern}' has low success rate")
        except Exception as e:
            print(f"Error optimizing command patterns: {e}")

    def cleanup_old_data(self):
        """Clean up old data to prevent excessive storage"""
        try:
            # Keep only last 1000 commands
            self.learning_data["successful_commands"] = self.learning_data["successful_commands"][-1000:]
            self.learning_data["failed_commands"] = self.learning_data["failed_commands"][-1000:]
            
            # Clean up command patterns with very low usage
            patterns_to_remove = []
            for pattern, data in self.learning_data["command_patterns"].items():
                total_usage = data["success_count"] + data["fail_count"]
                if total_usage < 2:  # Remove patterns used less than 2 times
                    patterns_to_remove.append(pattern)
            
            for pattern in patterns_to_remove:
                del self.learning_data["command_patterns"][pattern]
            
            # Clean up old error solutions (older than 30 days)
            current_time = datetime.now()
            for error_key in list(self.learning_data["error_solutions"].keys()):
                occurrences = self.learning_data["error_solutions"][error_key]["occurrences"]
                recent_occurrences = []
                for occurrence in occurrences:
                    timestamp = datetime.strptime(occurrence["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
                    if (current_time - timestamp).days < 30:
                        recent_occurrences.append(occurrence)
                
                if recent_occurrences:
                    self.learning_data["error_solutions"][error_key]["occurrences"] = recent_occurrences
                else:
                    del self.learning_data["error_solutions"][error_key]
            
            self.save_data()
        except Exception as e:
            print(f"Error cleaning up data: {e}")

    def get_command_suggestions(self, partial_command):
        """Get command suggestions based on learning"""
        suggestions = []
        try:
            words = partial_command.lower().split()
            if len(words) > 0:
                last_word = words[-1]
                for pattern in self.learning_data["command_patterns"]:
                    if pattern.startswith(last_word):
                        success_rate = self.get_pattern_success_rate(pattern)
                        if success_rate > 0.7:  # Only suggest successful patterns
                            suggestions.append(pattern)
        except Exception as e:
            print(f"Error getting suggestions: {e}")
        return suggestions[:5]  # Return top 5 suggestions

    def get_pattern_success_rate(self, pattern):
        """Calculate success rate for a pattern"""
        try:
            data = self.learning_data["command_patterns"][pattern]
            total = data["success_count"] + data["fail_count"]
            if total > 0:
                return data["success_count"] / total
        except Exception as e:
            print(f"Error calculating success rate: {e}")
        return 0

    def attempt_recovery(self, error, context):
        """Attempt to recover from errors automatically"""
        try:
            error_str = str(error)
            
            # Check if we've tried too many times
            if error_str in self.recovery_attempts:
                if self.recovery_attempts[error_str] >= self.max_recovery_attempts:
                    speak("Maximum recovery attempts reached. Please seek manual intervention.")
                    return False
                self.recovery_attempts[error_str] += 1
            else:
                self.recovery_attempts[error_str] = 1

            # Common error recovery strategies
            if "PermissionError" in error_str:
                return self.handle_permission_error(context)
            elif "FileNotFoundError" in error_str:
                return self.handle_missing_file(context)
            elif "ConnectionError" in error_str:
                return self.handle_connection_error(context)
            elif "MemoryError" in error_str:
                return self.handle_memory_error()
            elif "ModuleNotFoundError" in error_str:
                return self.handle_missing_module(error_str)
            
            # Check for process-related errors
            if any(term in error_str.lower() for term in ["process", "chrome", "browser", "driver"]):
                return self.handle_process_error(context)

            return False
            
        except Exception as e:
            print(f"Error in recovery attempt: {e}")
            return False

    def handle_permission_error(self, context):
        """Handle permission-related errors"""
        try:
            file_path = context.get("file_path", "")
            if file_path:
                # Try to fix file permissions
                subprocess.run(["attrib", "-R", file_path], shell=True)
                speak("Attempting to fix file permissions")
                return True
        except:
            return False

    def handle_missing_file(self, context):
        """Handle missing file errors"""
        try:
            file_path = context.get("file_path", "")
            if file_path:
                # Check if file exists in alternate locations
                alternate_paths = [
                    os.path.join(os.getcwd(), os.path.basename(file_path)),
                    os.path.join("Data", os.path.basename(file_path)),
                    os.path.join("Features", os.path.basename(file_path))
                ]
                
                for path in alternate_paths:
                    if os.path.exists(path):
                        speak(f"Found file in alternate location: {path}")
                        return True
                        
                speak("Creating necessary directories")
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                return True
        except:
            return False

    def handle_connection_error(self, context):
        """Handle connection-related errors"""
        try:
            speak("Detecting connection issues. Attempting to reconnect.")
            # Try to reset network connection
            subprocess.run(["ipconfig", "/release"], shell=True)
            time.sleep(2)
            subprocess.run(["ipconfig", "/renew"], shell=True)
            return True
        except:
            return False

    def handle_memory_error(self):
        """Handle memory-related errors"""
        try:
            speak("Clearing system memory")
            # Clear Python's memory
            import gc
            gc.collect()
            
            # Try to free up system memory
            if sys.platform == 'win32':
                subprocess.run("wmic process where name='python.exe' call setpriority 128", shell=True)
            
            return True
        except:
            return False

    def handle_missing_module(self, error_str):
        """Handle missing module errors"""
        try:
            # Extract module name from error
            module_name = error_str.split("'")[1]
            speak(f"Attempting to install missing module: {module_name}")
            
            # Try to install the module
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
            return True
        except:
            return False

    def handle_process_error(self, context):
        """Handle process-related errors"""
        try:
            speak("Attempting to clean up stuck processes")
            # Kill problematic processes
            for proc in psutil.process_iter():
                try:
                    if proc.name().lower() in ['chromedriver.exe', 'chrome.exe']:
                        proc.kill()
                except:
                    continue
            return True
        except:
            return False

    def load_feature_data(self):
        """Load learned features"""
        try:
            if os.path.exists(self.feature_data_path):
                with open(self.feature_data_path, 'r') as f:
                    self.feature_data = json.load(f)
            else:
                self.feature_data = {
                    "learned_commands": {},
                    "command_patterns": {},
                    "feature_suggestions": []
                }
                self.save_feature_data()
        except Exception as e:
            print(f"Error loading feature data: {e}")
            self.feature_data = {}
            
    def save_feature_data(self):
        try:
            with open(self.feature_data_path, 'w') as f:
                json.dump(self.feature_data, f, indent=4)
        except Exception as e:
            print(f"Error saving feature data: {e}")

    def learn_from_usage(self, command, success):
        """Learn from user command patterns"""
        try:
            if success:
                # Analyze command structure
                words = command.lower().split()
                if len(words) >= 2:
                    action = words[0]
                    target = ' '.join(words[1:])
                    
                    # Look for patterns
                    if action in ['open', 'play', 'search', 'check']:
                        self.suggest_new_feature(action, target)
                    
                    # Add command pattern to learning data
                    pattern = f"{action}_{target}"
                    if pattern not in self.feature_data["command_patterns"]:
                        self.feature_data["command_patterns"][pattern] = 1
                    else:
                        self.feature_data["command_patterns"][pattern] += 1
                    self.save_feature_data()
        except Exception as e:
            print(f"Error learning from usage: {e}")

    def suggest_new_feature(self, action, target):
        """Suggest new features based on usage patterns"""
        try:
            pattern = f"{action}_{target}"
            if pattern not in self.feature_data["learned_commands"]:
                # Check if this is a recurring pattern
                if pattern in self.feature_data["command_patterns"]:
                    count = self.feature_data["command_patterns"][pattern] + 1
                    if count > 5:  # If used more than 5 times
                        speak(f"I notice you often {action} {target}. Would you like me to create a shortcut for this?")
                        # Wait for response
                        response = self.wait_for_confirmation()
                        if response:
                            self.create_new_feature(action, target)
                    self.feature_data["command_patterns"][pattern] = count
                else:
                    self.feature_data["command_patterns"][pattern] = 1
                self.save_feature_data()
        except Exception as e:
            print(f"Error suggesting feature: {e}")

    def create_new_feature(self, action, target):
        """Create a new feature based on learned pattern"""
        try:
            command_name = f"{action}_{target}".replace(" ", "_")
            feature_code = self.generate_feature_code(action, target)
            
            # Save the new feature
            self.feature_data["learned_commands"][command_name] = {
                "action": action,
                "target": target,
                "code": feature_code,
                "created_at": str(datetime.now())
            }
            
            speak(f"I've created a new shortcut for {action} {target}")
            self.save_feature_data()
            
        except Exception as e:
            print(f"Error creating feature: {e}")

    def generate_feature_code(self, action, target):
        """Generate code for new feature"""
        if action == "open":
            return f"""
def {action}_{target.replace(" ", "_")}():
    from Automation.Web_Open import openweb
    openweb("{target}")
"""
        elif action == "play":
            return f"""
def {action}_{target.replace(" ", "_")}():
    from Automation.Play_Music_YT import play_music_on_youtube
    play_music_on_youtube("{target}")
"""
        # Add more patterns as needed
        return None

    def wait_for_confirmation(self):
        """Wait for user confirmation"""
        try:
            with open("input.txt", "r") as file:
                response = file.read().lower().strip()
                return any(word in response for word in ['yes', 'sure', 'okay', 'ha', 'create'])
        except:
            return False

    def execute_learned_command(self, command):
        """Execute a learned command"""
        try:
            command_name = command.replace(" ", "_")
            if command_name in self.feature_data["learned_commands"]:
                feature = self.feature_data["learned_commands"][command_name]
                exec(feature["code"])
                return True
            return False
        except Exception as e:
            print(f"Error executing learned command: {e}")
            return False 