import subprocess
import time
import sys

def run_load_tests():
    # Start locust in headless mode
    # Simulate 10 users with 1 user spawned per second
    cmd = [
        "locust", 
        "--headless", 
        "--users", "10",
        "--spawn-rate", "1",
        "--host", "http://localhost:5000",
        "--run-time", "1m"
    ]
    subprocess.run(cmd)

def run_bdd_tests():
    # Run behave tests
    subprocess.run(["behave"])

if __name__ == "__main__":
    # Start Flask app in background (you might want to do this separately)
    # flask_process = subprocess.Popen(["flask", "run"])
    # time.sleep(2)  # Wait for Flask to start
    
    try:
        print("Running Load Tests...")
        run_load_tests()
        
        print("\nRunning BDD Tests...")
        run_bdd_tests()
        
    finally:
        # flask_process.terminate()
        pass 