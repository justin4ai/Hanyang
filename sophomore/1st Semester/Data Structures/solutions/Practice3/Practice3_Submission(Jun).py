import sys

ADD = 'A'
DELETE = 'D'
FIND = 'F'

# cd "/mnt/c/Users/ahn01/HYU/Sophomore/1st Semester/Data Structures/Practices/Practice3"

class Student:
    def __init__(self, i, n, p=None):
        self.id = i
        self.name = n
        self.next = None
        pass


class Course:
    def __init__(self, l=[]):
        self.head = None
        pass

    #def __len__(self):
    #    return self.size

    #def isEmpty(self):
    #    return self.size == 0

    def addStudent(self, newID, newName):  # return true or false

        newNode = Student(newID, newName)
        cursor = self.head

        if cursor == None:
            self.head = newNode
            return True

        if cursor.id > newID:  # At the beginning

            newNode.next = cursor
            self.head = newNode
            return True

        elif cursor.id == newID:
            print("Addition Failed")
            return False

        while True:

            if cursor.next == None:  # Reach the end of the linked list
                cursor.next = newNode
                return True

            if cursor.id < newID:

                if cursor.next.id > newID:  # Time to add

                    newNode.next = cursor.next
                    cursor.next = newNode
                    return True

                elif cursor.next.id == newID:  # Reach the end of the linked list
                    print("Addition Failed")
                    return False

                else:
                    cursor = cursor.next




        pass

    def deleteStudent(self, queryID):  # return true or false
        cursor = self.head

        if cursor == None:
            print("Deletion Failed")
            return False

        if cursor.id == queryID:  # At the beginning

            if cursor.next != None:
                temp = self.head
                self.head, temp = cursor.next, None
                return True

            else:
                self.head = None
                return True

        else:

            if cursor.next == None:
                print("Deletion failed")
                return False

        preNode = cursor
        cursor = cursor.next

        while True:

            if cursor.id == queryID:

                if cursor.next != None:
                    preNode.next = cursor.next
                    cursor = None
                    return True


                else:
                    preNode.next = None
                    cursor = None
                    return True

            if cursor.next == None:
                break

            preNode = cursor
            cursor = cursor.next

        print("Deletion Failed")
        pass

    def find(self, queryID):  # gotta return the node itself (if not exist, return None)
        cursor = self.head

        if cursor == None:
            print(f"Search failed.")
            return None

        while True:
            if int(cursor.id) == queryID:
                return cursor

            if cursor.next == None:
                print(f"Search failed.")
                return None

            cursor = cursor.next
        pass

    def write(self, outFile):  # For 'A' and 'D'

        lineToWrite = ''
        cursor = self.head

        if cursor == None:
            print("")
            outFile.write('\n')
            return

        while True:

            lineToWrite += str(cursor.id)
            lineToWrite += ' '
            lineToWrite += cursor.name
            lineToWrite += ' '

            if cursor.next == None:
                print(f"{lineToWrite}")
                outFile.write(lineToWrite + '\n')
                break

            cursor = cursor.next

        pass


if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("Correct usage: [program] [input] [output]")

    course = Course()
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
    with open(sys.argv[2], 'w') as outFile:
        print(outFile)
        for line in lines:
            words = line.split()
            op = words[0]  # Alphabet for the task
            if op == ADD:
                if len(words) != 3:
                    raise Exception("ADD: invalid input")
                i, n = int(words[1]), words[2]
                if course.addStudent(i, n):
                    course.write(outFile)
                else:
                    outFile.write("Addition failed\n")
            elif op == DELETE:
                if len(words) != 2:
                    raise Exception("DELETE: invalid input")
                i = int(words[1])
                if course.deleteStudent(i):
                    course.write(outFile)
                else:
                    outFile.write("Deletion failed\n")
            elif op == FIND:
                if len(words) != 2:
                    raise Exception("DELETE: invalid input")
                i = int(words[1])  # Given ID
                found = course.find(i)
                if not found:
                    outFile.write("Search failed\n")
                else:
                    print(str(found.id) + " " + found.name) # for check
                    outFile.write(str(found.id) + " " + found.name + "\n")
            else:
                raise Exception("Undefined operator")

