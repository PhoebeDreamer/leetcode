class Solution:
    def tree2str(self, t):
        if not t:
            return ""

        ans = str(t.val)

        if t.left and t.right:
            ans += "(" + self.tree2str(t.left) + ")"
            ans += "(" + self.tree2str(t.right) + ")"
        elif t.left and not t.right:
            ans += "(" + self.tree2str(t.left) + ")"
        elif not t.left and t.right:
            ans += "()" + "(" + self.tree2str(t.right) + ")"

        return ans