import pygame, json


path = "/home/pi/dealguy/"


def _load_json(file_path):
    json_file = open(file_path, "r")
    json_str = json_file.read()
    json_file.close()
    return json.loads(json_str)


def _save_to_json(file_path, object):
    json_file = open(file_path, "w")
    json.dump(object, json_file)
    json_file.close()


def play(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def get_next_sound(sound_type):
    history_json = _load_json(path + "sounds/soundHistory.json")
    previous_index = history_json[sound_type]
    sound_json = _load_json(path + "sounds/sounds.json")
    sound_list = sound_json[sound_type + "Files"]
    new_index = previous_index + 1 if (len(sound_list) >= previous_index + 2) else 0
    history_json[sound_type] = new_index
    _save_to_json(path + "sounds/soundHistory.json", history_json)
    return sound_list[new_index]
