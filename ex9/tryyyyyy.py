class Shelf:
    def __init__(self):
        self.__aim = []


    def place_item_on(self, item, thing):
        if thing == self:
            self.__aim.append([item])
            return
        for a in self.__aim:
            if a == thing:
                a.append(item)
                return
        return 'False'


    def remove_item(self, item):
        for b in self.__aim:
            if b[-1] == item:
                b[-1].pop()
                if not b:
                    self.__aim.remove(b)
                return
        return 'sos'


    def __str__(self):
        string = ''
        for i in self.__aim:
            string += 'in'.join(i[::-1]) + '\n'
            return string
        return








        #
        #
        # for i, v in enumerate(self.__aim):
        #     t = ''
        #     for j , vv in v:
        #         if vv != v[-1]:
        #             t += vv + 'on'
        #         else:
        #             t += vv + '\n'
        #     last += t
        # return last
        #



# ממשו מחלקה Shelf המדמה מדף עליו ניתן להניח חפצים בערמות.
#
# יש לתמוך בארבעת הפעולות הבאות:
#
# 1. יצירה של אובייקט מהמחלקה (ללא פרמטרים נוספים).
#
# 2. השמת דבר מה על המדף, באמצעות מתודה בשם  place_item_on, המקבלת מחרוזת המייצגת פריט בשם item, ופרמטר בשם thing, ומניחה את הפריט על המדף באופן הבא:
#
# אם ערכו של thing הוא המדף עצמו - נוצרת ערימה חדשה על המדף לצד ערימות אחרות שקיימות כבר.
# אם ערכו של thing הוא חפץ שמונח בראש אחת הערימות הקיימות כבר על המדף, יש להניח את הפריט בראש ערימה זו.
# במקרים אחרים יש להחזיר הודעת שגיאה לבחיתרכם.
# 3. הסרת חפץ מראש הערימה, באמצעות מתודה בשם remove, המקבלת מחרוזת המייצגת פריט בשם item, ומסירה אותו מראש הערימה בה הוא מופיע, אם קיימת כזו. אם הפריט לא מופיע בראש ערימה - יש להחזיר הודעת שגיאה לבחירתכם.
#
# 4. הדפסת המדף - קריאה לפונקציה print עם אובייקט מטיפוס מדף תרגום להדפסה של כל הערימות שעל המדף. כל ערימה תודפס בשורה חדשה. הדפסת ערימה תתחיל מהאיבר העליון בה, ובין כל שני פריטים בערימה תודפס המחרוזת " on ".
#
#
#
# ניתן להניח שפריט מסויים יונח על המדף פעם אחת לכל היותר