class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stack: 一端进出,后进先出(LIFO)
        # Queue: 一端进另一端出,先进先出(FIFO)
        # monotonic deque: (Double-Ended Queue) 两端都能进出
        # 本题用 monotonic deque -> 维护最大值，也能维护次大值

        dq = deque()
        ans = []

        for index, num in enumerate(nums):
            # 1) 维护单调性：队尾对应值 <= 新值，就从队尾弹掉
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(index)
            # 2) 队头下标滑出窗口了（不在 [j-k+1, j] 内），从队头弹掉
            # 窗口覆盖index范围: [index - k + 1, index]
            if dq[0] <= index - k:
                dq.popleft()

            # 3) 窗口形成后（j 到达第 k-1 个位置起），记录队头 = 当前窗口最大值
            # 判断"窗口有没有凑满 k 个元素"。
            # 窗口要装满 k 个,右边界至少得走到第 k 个位置,也就是下标 k-1。
            # 在那之前,窗口还没成形,不该输出答案。
            if index >= k - 1:
                ans.append(nums[dq[0]])

        return ans