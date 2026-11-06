class ContextManager:
    def __init__(self, file):
        self.filename = open(file, 'w')
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        if self.level == 0:
            self.filename.close()

    def writer(self, text):
        tabs = '\t' * self.level
        self.filename.write(f'{tabs}{text}\n')

with ContextManager('12.txt') as f:
    f.writer('1 otsup')
    f.writer('1 otstup')
    with f:
        f.writer('2 otstupa')
        with f:
            f.writer('3 otstupa')
    f.writer('1 otstup')
