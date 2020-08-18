#5-15 從靠近指定長度的空格剪裁,來縮減字串的函式

def clip(text = str,max_len:'int > 0' = 80) -> str:
    """Return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind('',0,max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text,rfind('',max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  #找不到空格
        end = len(text)
    return text[:end].rstrip()

