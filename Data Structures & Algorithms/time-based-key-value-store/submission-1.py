class TimeMap:

    def __init__(self):
        self.my_dict={}

        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not (key in self.my_dict):
            self.my_dict[key]={}
        
        if not (timestamp in self.my_dict[key]):
            self.my_dict[key][timestamp]=[]

        self.my_dict[key][timestamp].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.my_dict:
            while timestamp>=0:
                if timestamp in self.my_dict[key]:
                    return self.my_dict[key][timestamp][-1]
                timestamp=timestamp-1
        
        return ''
