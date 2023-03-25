from enum import Enum

class webDriverWaitEnum(Enum):
    presence_of_element_located = "presence_of_element_located"
    visibility_of_element_located = "visibility_of_element_located"
    element_to_be_clickable = "element_to_be_clickable"


class withIDorXPATH(Enum):
    by_id = "BY_ID"
    by_xpath = "BY_XPATH"
    by_className="BY_CLASSNAME"



class waitSecond(Enum):
    low = 3
    middle = 5
    long = 10


class prgoramProcess(Enum):
    Start = "Start"
    Continue = "Continue"
    Stop = "Stop"

class scroolPosition(Enum):
    UP = "UP"
    DOWN = "DOWN"
