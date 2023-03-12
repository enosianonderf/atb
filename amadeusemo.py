from random import choice


def emos(emo_point):
    global dirr
    smile = [
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuSmile/CRS_JLE_40000300.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuSmile/CRS_JLE_40000301.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuSmile/CRS_JLE_40000302.png"]
    emb = [
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuEmb/CRS_JLE_40000200.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuEmb/CRS_JLE_40000201.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuEmb/emb1.png"]
    neu = [
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuNeutral/CRS_JLD_40000901.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuNeutral/neu1.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuNeutral/neu2.png"]
    cry = [
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuCry/cry1.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuCry/cry3.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuCry/cry2.png"]
    sad = [
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuSad/CRS_JLE_40000601.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuSad/CRS_JLE_40000600.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuSad/CRS_JLE_40000700.png"]
    angry = [
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuAngry/CRS_JLE_40000400.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuAngry/CRS_JLE_40000401.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuAngry/CRS_JLE_40000402.png"]
    happy = [
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuFun/fun4.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuFun/fun5.png",
        "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuFun/fun6.png"]
    if emo_point >= 90 and emo_point <= 100:
        dirr = choice(happy)
    elif emo_point >= 80 and emo_point < 90:
        dirr = choice(smile)
    elif emo_point >= 70 and emo_point < 80:
        dirr = choice(emb)
    elif emo_point >= 50 and emo_point < 70:
        dirr = choice(neu)
    elif emo_point >= 40 and emo_point < 50:
        dirr = choice(sad)
    elif emo_point >= 20 and emo_point < 40:
        dirr = choice(angry)
    elif emo_point >= 0 and emo_point < 20:
        dirr = choice(cry)
    elif emo_point == -1:
        dirr = "https://raw.githubusercontent.com/enosianonderf/amadeussecondbot/master/amadeussecondbot/amadeusemo/KurisuSleep/sleep1.png"
    return dirr
