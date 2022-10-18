import convert_format
import parsing_format

FORMATS = [
    { 
        'formatDataDelimeter': '\n', 
        'userDataDelimeter': ';', 
        'userPropertiesDelimeter': ',',  

    },
    {
        'formatDataDelimeter': '\t',
        'userDataDelimeter': ';',
        'userPropertiesDelimeter': ',',
    },
    {
        'formatDataDelimeter': '%',
        'userDataDelimeter': ';',
        'userPropertiesDelimeter': ',',
    }

