import uicamera
import devicecom2
import target_controller
import threading

def run():
    out = tgt_ctrl.get_latest_coords()
    if out:
        print("From Serial: {out}".format(out=out))
        

def main():
    global tgt_ctrl

    tgt_ctrl = target_controller.TargetController()

    out_thread = threading.Thread(target=run, daemon=True)
    out_thread.start()

    c_ui = uicamera.UI(tgt_ctrl)
 

 

if __name__ == "__main__":
    main()       



