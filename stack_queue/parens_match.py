# encoding:utf-8

from SStack import SStack

"""括号配对检查函数，text是被检查的正文串"""
def check_parens(text):
    parens = "()[]{}"    # 所有括号字符
    open_parens = "([{"  # 开括号字符
    opposite = {')':'(', ']':'[', '}':'{'}  # 表示配对关系的字典
    
    """括号生成器，每次调用返回text里的下一括号及其位置"""
    def parentheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
            
    st = SStack()               # 保存括号的栈
    
    for pr, i in parentheses(text):   # 对text里各括号和位置迭代
        if pr in open_parens:        # 开括号，压进栈并继续
            st.push(pr)
        elif st.pop() != opposite[pr]:  # 匹配失败
            print("Unmatching is found at", i, "for", pr)
            return False
        # else:括号匹配成功，什么也不做，继续
        
    print("All parentheses are correctly matched.")
    return True
 
if __name__ == '__main__':
    print(check_parens('(abc{lmn}[[])'))   
