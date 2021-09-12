import live_data_summary
import tool_function as tf


# room_id, live_date, live_road, live_type = tf.get_arg()

def process_live_data(room_id, live_date):
    target_path = "/home/admin/public/data/"
    live_road = "%s_%s" % (live_date, room_id)
    live = live_data_summary.live_summary(my_room_id=room_id, my_live_date=live_date,
                                      my_live_road=live_road, target_path = target_path)
    live.get_everyday_live_stats()
    print("Everything gets done!")

if __name__ == '__main__':
    process_live_data('22634198', '2021_9_10')