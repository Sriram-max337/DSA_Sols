class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        dirs = []

        for p in parts:
            if p=="" or p==".":
                continue
            if p=="..":
                if dirs:
                    dirs.pop()
            else:
                dirs.append(p)

        return "/"+"/".join(dirs)
