from crazy_functions.agent_fns.pipe import PluginMultiprocessManager, PipeCom

class EchoDemo(PluginMultiprocessManager):
    def subprocess_worker(self, child_conn):
        # ⭐⭐ 子进程
        self.child_conn = child_conn
        while True:
            msg = self.child_conn.recv() # PipeCom
            if msg.cmd == "user_input":
                # wait futher user input
                self.child_conn.send(PipeCom("show", msg.content))
                wait_success = self.subprocess_worker_wait_user_feedback(wait_msg="我准备好处理下一个问题了.")
                if not wait_success:
                    # wait timeout, terminate this subprocess_worker
                    break
            elif msg.cmd == "terminate":
                self.child_conn.send(PipeCom("done", ""))
                break
        print('[debug] subprocess_worker terminated')