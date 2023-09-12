import socket
import threading
import time
import TwitchConnect

global user
global message
global user_count
global message_count

user_count = {}
message_count = 0

def update_stats(user, message):
    """
    Update user and message statistics.
    """
    global user_count
    global message_count

    # Update user statistics
    if "JOIN #" in user:
                    user_count += 1  # Increment viewer_count when a user joins
    elif "PART #" in user:
                    user_count -= 1  # Decrement viewer_count when a user leaves

    # Update message count
    message_count += 1

def display_stats():
    """
    Display user and message statistics.
    """
    while True:
        # Display the number of messages sent by each user and total message count
        print("----- User Message Statistics -----")
        for user, count in user_count.items():
            print(f"{user}: {count} messages")

        print(f"Total User watching: {user_count}")
        print("\n")

        print(f"Total Messages: {message_count}")
        print("\n")

        # Sleep for 30 seconds before displaying statistics again
        # Display statistics every 10 seconds (adjust as needed)
        time.sleep(30)

# Start a thread to display statistics
t2 = threading.Thread(target=display_stats)
t2.start()
