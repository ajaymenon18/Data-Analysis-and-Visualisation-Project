import justpy as jp
import justpy as jp

def app():
    wep = jp.QuasarPage()
    h1 = jp.QDiv(a = wep, text = "Analysis of course reviews", classes = "text-h1 text-center q-pa-md ")
    p1 = jp.QDiv(a = wep, text = "These graphs represent course review analysis")
    return wep

jp.justpy(app)