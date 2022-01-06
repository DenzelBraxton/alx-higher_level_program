#!/usr/bin/python3
"""Module base.
Defines a Base of all other classes in this project.
"""

import json
import os
import csv


class Base:
    """This is a class
        It has a private class attribute called __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This is an initialization of the instance of the base class

        Args:
            id: It takes id as an argument and is set to None. This is the id of the instance
        """

        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """This function update the class Base and returns the JSON string
        
        Args:
            - list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return []
        if (type(list_dictionaries) != list or not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """It writes the JSON string representation of list_objs to a file
        
        Args:
            - list_objs:  list of instances who inherits of Base
        """

        if list_objs is None or list_objs == []:
            jasonstr = "[]"
        else:
            jasonstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
                f.write(jasonstr)
    
    @staticmethod
    def from_json_string(json_string):
        """it returns the list of the JSON string representation json_string
        
        Args:
            - json_string: this is a string representing a list of dictionaries
        """

        x = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            x = json.loads(json_string)
        return x
    
    @classmethod
    def create(cls, **dictionary):
        """It returns an instance with all attributes already set
        
        Args:
            - **dictionary: it  can be thought of as a double pointer to a dictionary
            - Returns: instance created
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """It returns a list of instances"""

        filename = cls.__name__ + ".json"
        x = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    x.append(cls.create(**d))
        return x
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """it serializes and deserializes in CSV
            It save it in a file
        
        Args:
            - list_objs: list of instances
        """

        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)
    
    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file.

        Returns: list of instances
        """

        filename = cls.__name__ + ".csv"
        l = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        l.append(i)
        return l
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a Turtle window and draws rectangles and squares.

        Args:
            - list_rectangles: list of Rectangle instances
            - list_squares: list of Square instances
        """

        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("violet")
        t.shape("square")
        t.pensize(8)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)
    
    @staticmethod
    def draw_rect(t, rect):
        """Helper method that draws a Rectangle
        or Square.
        """

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)