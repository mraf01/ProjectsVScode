import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"time elapsed: {elapsed_time:.5f}")


if __name__ == "__main__":
    with Timer():
        time.sleep(1)