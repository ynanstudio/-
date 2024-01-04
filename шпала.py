 # __     ___   _          _   _ 
 # \ \   / / \ | |   /\   | \ | |
 #  \ \_/ /|  \| |  /  \  |  \| |
 #   \   / | . ` | / /\ \ | . ` |
 #    | |  | |\  |/ ____ \| |\  |
 #    |_|  |_| \_/_/    \_\_| \_|
# Copyright 2023 YNAN STUDIO

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import winreg
import os
import shutil

def resource_path(relative_path):#функция которая определяет путь к файлу который находится внутри exe(который добавили в патч при билде)
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#=========================================================
new_sound_path =  'C:\\temp\\шпала\\шпала.wav' #Путь куда будем перекидывать файл
os.makedirs('C:\\temp\\шпала', exist_ok=True) #Создаем папки которых может по дороге к new_sound_path не оказаться
shutil.copyfile(resource_path('шпала.wav'), new_sound_path) #Копируем файл в new_sound_path
sound_event_path = r"AppEvents\Schemes\Apps\.Default" #Путь в реестре в котором находятся ивенты и путь к вопроизводимым файлам
#=========================================================
def set_system_sound(event_name, sound_path):
    try:
        key = winreg.HKEY_CURRENT_USER
        subkey = sound_event_path + "\\" + event_name + "\\.Current"
        with winreg.CreateKey(key, subkey) as reg_key:
            winreg.SetValueEx(reg_key, "", 0, winreg.REG_SZ, sound_path)
    except:
        return

def get_system_sound_events():
    try:
        key = winreg.HKEY_CURRENT_USER
        subkey = sound_event_path
        with winreg.OpenKey(key, subkey) as reg_key:
            event_names = []
            index = 0
            while True:
                try:
                    event_name = winreg.EnumKey(reg_key, index)
                    event_names.append(event_name)
                    index += 1
                except OSError:
                    break
            return event_names
    except Exception as e:
        return []
system_sound_events = get_system_sound_events()
for event in system_sound_events:
    set_system_sound(event, new_sound_path)