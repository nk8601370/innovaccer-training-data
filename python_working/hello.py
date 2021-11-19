import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    
    
def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    b=event.src_path
    file = open(b, "rt")
    data = file.read()
    words = data.split()
    print('Number of words in text file :', len(words))
    
def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")
    

def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
    
    
my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved
    
path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    
    
my_observer.start()
try:
    while True:
       time.sleep(1)
except KeyboardInterrupt:
   my_observer.stop()
   my_observer.join()



# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
  
  
# class OnMyWatch:
#     # Set the directory on watch
#     watchDirectory = "/home/adminroot/Desktop/python_working"
  
#     def __init__(self):
#         self.observer = Observer()
  
#     def run(self):
#         event_handler = Handler()
#         self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
#         self.observer.start()
#         try:
#             while True:
#                 time.sleep(5)
#         except:
#             self.observer.stop()
#             print("Observer Stopped")
  
#         self.observer.join()
  
  
# class Handler(FileSystemEventHandler):
  
#     @staticmethod
#     def on_any_event(event):
#         if event.is_directory:
#             return None
  
#         elif event.event_type == 'created':
#             # Event is created, you can process it now
#             b=event.src_path
#             file = open(b, "rt")
#             data = file.read()
#             words = data.split()
#             print('Number of words in text file :', len(words))
#             print("Watchdog received created event - % s." % event.src_path)
#         elif event.event_type == 'modified':
#             # Event is modified, you can process it now
#             a=event.src_path
#             file = open(a, "rt")
#             data = file.read()
#             words = data.split()
#             print('Number of words in text file :', len(words))
#             print("Watchdog received modified event - % s." % event.src_path)
              
  
# if __name__ == '__main__':
#     watch = OnMyWatch()
#     watch.run()