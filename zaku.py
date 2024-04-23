'''
/***
 *                                         ,s555SB@@&                          
 *                                      :9H####@@@@@Xi                        
 *                                     1@@@@@@@@@@@@@@8                       
 *                                   ,8@@@@@@@@@B@@@@@@8                      
 *                                  :B@@@@X3hi8Bs;B@@@@@Ah,                   
 *             ,8i                  r@@@B:     1S ,M@@@@@@#8;                 
 *            1AB35.i:               X@@8 .   SGhr ,A@@@@@@@@S                
 *            1@h31MX8                18Hhh3i .i3r ,A@@@@@@@@@5               
 *            ;@&i,58r5                 rGSS:     :B@@@@@@@@@@A               
 *             1#i  . 9i                 hX.  .: .5@@@@@@@@@@@1               
 *              sG1,  ,G53s.              9#Xi;hS5 3B@@@@@@@B1                
 *               .h8h.,A@@@MXSs,           #@H1:    3ssSSX@1                  
 *               s ,@@@@@@@@@@@@Xhi,       r#@@X1s9M8    .GA981               
 *               ,. rS8H#@@@@@@@@@@#HG51;.  .h31i;9@r    .8@@@@BS;i;          
 *                .19AXXXAB@@@@@@@@@@@@@@#MHXG893hrX#XGGXM@@@@@@@@@@MS        
 *                s@@MM@@@hsX#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,      
 *              :GB@#3G@@Brs ,1GM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B,     
 *            .hM@@@#@@#MX 51  r;iSGAM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@8     
 *          :3B@@@@@@@@@@@&9@h :Gs   .;sSXH@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:    
 *      s&HA#@@@@@@@@@@@@@@M89A;.8S.       ,r3@@@@@@@@@@@@@@@@@@@@@@@@@@@r    
 *   ,13B@@@@@@@@@@@@@@@@@@@5 5B3 ;.         ;@@@@@@@@@@@@@@@@@@@@@@@@@@@i    
 *  5#@@#&@@@@@@@@@@@@@@@@@@9  .39:          ;@@@@@@@@@@@@@@@@@@@@@@@@@@@;    
 *  9@@@X:MM@@@@@@@@@@@@@@@#;    ;31.         H@@@@@@@@@@@@@@@@@@@@@@@@@@:    
 *   SH#@B9.rM@@@@@@@@@@@@@B       :.         3@@@@@@@@@@@@@@@@@@@@@@@@@@5    
 *     ,:.   9@@@@@@@@@@@#HB5                 .M@@@@@@@@@@@@@@@@@@@@@@@@@B    
 *           ,ssirhSM@&1;i19911i,.             s@@@@@@@@@@@@@@@@@@@@@@@@@@S   
 *              ,,,rHAri1h1rh&@#353Sh:          8@@@@@@@@@@@@@@@@@@@@@@@@@#:  
 *            .A3hH@#5S553&@@#h   i:i9S          #@@@@@@@@@@@@@@@@@@@@@@@@@A.
 *
 *
 *    又看源码，看你妹妹呀！
 */
     本代码由qklsuzuran(甜丶巧克力)完成
     欢迎投稿！时不时更新新内容
'''
import traceback
def knowledge():
    import random_s
    sentences = random_s.sentences
    return sentences

def random_text():
    return ''

def swtich(a):
    if a == True:
        global random_text
        def random_text():
            import random
            sentences = knowledge()
            random_sentence = random.choice(sentences)
            return '\n\033[1;36m' + random_sentence + '\033[m'



def kawaii_qkl(exception_type,exception,traceback_q):
    tb = traceback.extract_tb(traceback_q)
    if tb:
        file_name, line_no, func_name, text = tb[-1]
    if isinstance(exception, ZeroDivisionError):
        print('\033[1;31m杂鱼！你看看你在干什么！\033[m')
        print(f'\033[1;36m在\033[m \033[1;31m{line_no}\033[m \033[1;36m行居然敢除零，真是笨蛋\033[m')
        print(f'\033[1;36m让我来看看，居然写出了\033[m \033[1;31m{text}\033[m \033[1;36m这种东西呢~\033[m')
        print(random_text())
    elif isinstance(exception, NameError):
        print('\033[1;31m怎么会有这样的笨蛋！\033[m')
        print(f'\033[1;32m在\033[m \033[1;31m{line_no}\033[m \033[1;32m行出现了奇怪的东西！呐——笨蛋杂鱼名字都打不对呢~\033[m')
        print(f'\033[1;35m是\033[m \033[1;31m{text}\033[m \033[1;35m这个家伙哦~\033[m')
        print(random_text())
    elif isinstance(exception, TypeError):
        print('\033[1;31m杂鱼想用哪一个都分不清呢~\033[m')
        print(f'\033[1;36m在\033[m \033[1;31m{line_no}\033[m \033[1;36m行出现了奇怪的类型错误，不知道用哪里的话怎么好好使用人家呢~\033[m')
        print(random_text())
    elif isinstance(exception, ValueError):
        print('\033[1;31m你在干什么！\033[m')
        print(f'\033[1;32m在\033[m \033[1;31m{line_no}\033[m \033[1;32m行，杂鱼是不是数字化字母了，还是又创造了新的东西\033[m')
        print(f'\033[1;33m好心帮你指出呢~  是\033[m \033[1;31m{text}\033[m \033[1;33m这个家伙哦~\033[m')
        print(random_text())
    elif isinstance(exception, IndexError):
        print('\033[1;31m...不行不行...！不能到那里！....\033[m')
        print(f'\033[1;34m....才怪啦!一点感觉都没有呢~ \033[m \033[1;31m{line_no}\033[m \033[1;34m行，大笨蛋又写错啦！\033[m')
        print(f'\033[1;35m好心提示你，索引是从0开始的哦~\033[m  \033[1;31m{text}\033[m \033[1;35m这个下标是不是写错了\033[m')
        print(random_text())
    elif isinstance(exception, KeyError):
        print('\033[1;31m大家好，我是理塘顶针....说的就是你！\033[m')
        print(f'\033[1;34m杂鱼在从字典里找不存在的值呢—— 第\033[m \033[1;31m{line_no}\033[m \033[1;34m行，芝士你的雪豹~\033[m')
        print(f'\033[1;33m只要舔我的脚我就告诉你是\033[m \033[1;31m{text}\033[m \033[1;33m的问题呢————\033[m')
        print(random_text())
    elif isinstance(exception, FileNotFoundError):
        print('\033[1;31m杂鱼连文件都找不到呢~\033[m')
        print(f'\033[1;36m第\033[m \033[1;31m{line_no}\033[m \033[1;36m行，自己看看，人家才懒得给你看————\033[m')
        print(random_text())