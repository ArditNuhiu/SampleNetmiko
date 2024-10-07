import concurrent.futures as cf
import time
import netmiko


def task_get_device_promt(device, cred):
    net_connect = netmiko.ConnectHandler(
        device_type="cisco_ios",
        host=device,
        username="test",
        password="password",
    )
    print(net_connect.find_prompt())
    net_connect.disconnect()


def executor_starter(devices, threads):
    with cf.ThreadPoolExecutor(max_workers=threads) as thread_executer:
        for device in devices:
            time.sleep(0.5)
            thread_executer.submit(task_get_device_promt, device)


def main():
    devices = ["sw-01", "sw-02"]
    executor_starter(devices, 64)


if __name__ == "__main__":
    main()
    exit()
