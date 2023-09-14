class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            self.head = new_node
            self.head.next_node = temp_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def to_list(self):
        list_format = []
        node = self.head
        while node:
            list_format.append(str(node.data))
            node = node.next_node
        return list_format

    def get_data_by_id(self, data):
        list_format = []
        node = self.head
        while node:
            try:
                list_format.append(dict(node.data))
            except:
                print('Данные не являются словарем или в словаре нет id')
            node = node.next_node
        for piece in list_format:
            if piece['id'] == data:
                return piece

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
