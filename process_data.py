import pdb
import requests
import threading
import time
from collections import namedtuple
from pprint import pprint
from datetime import date
from bilibili_live_data_summary import process_live_data
import json

class process_data(object):
    def __init__(self):

        self.vtb_info = namedtuple("vtb_info", 'uid room_id is_live')

        self.asoul_uid_dict = {
            '嘉然今天吃什么': self.vtb_info('672328094', '22637261', 0),
            '向晚大魔王':self.vtb_info('672346917', '22625025', 0),
            '乃琳Queen':self.vtb_info('672342685', '22625027', 0),
            '贝拉kira':self.vtb_info('672353429', '22632424', 0),
            '珈乐Carol':self.vtb_info('351609538', '22634198', 0),
            'A-SOUL_Official':self.vtb_info('703007996', '22632157', 0)
        }

    def obtain_single_vtb_room_info_via_uid(self, uid):
        contents = requests.get(f'https://api.vtbs.moe/v1/detail/{uid}').json()
        return f"【{contents['title']}】"

    def obtain_all_live_roomid(self):
        contents = requests.get(f'https://api.vtbs.moe/v1/living').json()
        return contents

    def obtain_single_vtb_room_status(self, roomid, room_id_live_list):
        if int(roomid) in room_id_live_list:
            return 1 # 开播
        else:
            return 0 # 未开播

    def update_room_status(self):
        room_id_live_list = self.obtain_all_live_roomid()
        for name, vtb_info in self.asoul_uid_dict.items():
            current_room_status = self.obtain_single_vtb_room_status(vtb_info.room_id, room_id_live_list)
            previous_room_status = vtb_info.is_live
            if current_room_status == 1 and previous_room_status == 0:
                title = self.obtain_single_vtb_room_info_via_uid(vtb_info.uid)
                print(f"{name} 上播啦， 直播间标题为：{title}")

            if current_room_status == 0 and previous_room_status == 1:
                room_id = vtb_info.room_id
                live_date = self.current_date()
                if not title:
                    title = "未知标题"

                print(f"{name} 下播啦, 正在处理{room_id}数据, 时间：{live_date}, 标题：{title}")

                process_live_data(room_id, live_date)

                target_path = "/home/admin/public/active/"
                # Load live list
                live_json_readin = target_path + 'real_live_list.json'
                with open(live_json_readin) as json_file:
                    live_list = json.load(json_file)

                # Push new live info
                live_list.insert(0, live_date + "&" + room_id + "&" + title)
                # save the updated results
                with open(f"{target_path}/real_live_list.json", "w", encoding='utf8') as outfile:
                    json.dump(live_list, outfile, ensure_ascii=False)

            'Update the room status'
            self.asoul_uid_dict[name] = self.asoul_uid_dict[name]._replace(is_live=current_room_status)
        # pprint(self.asoul_uid_dict)

    def begin_update_data_periodically(self):
        timerThread = threading.Thread(target=self.timer_func)
        timerThread.start()

    def timer_func(self):
        while True:
            self.update_room_status()
            time.sleep(20)

    def current_date(self):
        today = date.today()
        # mm/dd/y
        return today.strftime("20%y_%-m_%-d")

if __name__ == '__main__':
    PD = process_data()
    # PD.obtain_single_vtb_room_info_via_uid('672328094')
    # pdb.set_trace()
    # PD.current_date()
    PD.begin_update_data_periodically()