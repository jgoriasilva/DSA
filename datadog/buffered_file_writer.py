"""
Problem:
Design a BufferedFileWriter class that writes data to a file 
    but buffers the writes to minimize I/O operations. 
The buffer should be flushed to the file either when it reaches a certain size
     or when the flush() method is called explicitly.

Solution:
I need a class that will handle this problem. 
The class will have a write method, 
    which will append what is supposed to be written to an array.
It will also have a flush method, 
    which will take everything that is in the array and write to a file.
The flush array will be called automatically once a max_size of the array, 
    specified as an attribute is reached.
The class will have an attribute which is the file path to which it should write.
"""

class BufferedFileWriter():
    """
    Class implementing file writing using buffer.
    
    Attributes:
        file_path (str): The path to the file where data will be written.
        buffer_size (int): Maximum number of data to be held at buffer before it flushes.
        buffer (list[str]): Buffer containing data to be written.
    """
    def __init__(self, file_path: str, buffer_size: int = 10):
        """
        Initializes class with specified file path and buffer size.

        Args:
            file_path (str): The path to the file where data will be written.
            buffer_size (int): Maximum number of data to be held at buffer before it flushes.
        """
        self.file_path = file_path
        self.buffer_size = buffer_size
        self.buffer = []

    def write(self, data: str) -> None:
        """
        Writes data to buffer.

        If size of buffer exceeds the maximum, flushes buffer into file.

        Args:
            data (str): Data to be written to buffer.
        """
        self.buffer.append(data)
        if len(self.buffer) >= self.buffer_size:
            self.flush()

    def flush(self) -> None:
        """
        Flushes data from buffer into file.
        """
        size = len(self.buffer)
        if size > 0:
            with open(self.file_path, 'a', encoding='utf-8') as file:
                for data in self.buffer:
                    file.write(data + '\n')
            self.buffer = []
            print(f'{size} lines have been written to {self.file_path}')

def main():
    file_path = input('File to write to: ')
    buffer_size = int(input('Buffer size (int): '))
    writer = BufferedFileWriter(file_path, buffer_size)

    while True:
        data = input('Data to be written: ')
        if data == 'q': break
        writer.write(data)

    writer.flush()

if __name__ == '__main__':
    main()