import tkinter as tk
import os
import subprocess

class EstonianTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Эстонский тест A2-С1 уровня")
        self.root.geometry("1000x800")
        # Запрещаем изменение размеров окна
        self.score = 0
        self.current_question = 0
        self.answers = []
        self.questions = [
            {
                "question": "Tööpäev _______ kell kaheksa.",
                "options": ["algab", "algatab", "alustab"],
                "answer": "algab"
            },
            {
                "question": "Mida ta selle all _______?",
                "options": ["silmas pidas", "meeles pidas", "aru pidas"],
                "answer": "silmas pidas"
            },
            {
                "question": "Teie lehetellimus _______ varsti.",
                "options": ["aegub", "aeglustub", "ajab"],
                "answer": "aegub"
            },
            {
                "question": "Järgmine kokkutulek on kahe aasta _______.",
                "options": ["tagant", "pärast", "järelt"],
                "answer": "tagant"
            },
            {
                "question": "Ma _______ oma käekoti bussi.",
                "options": ["mäletasin", "unistasin", "unustasin"],
                "answer": "unustasin"
            },
            {
                "question": "Leping tuleb kinnitada _______.",
                "options": ["pealkirjaga", "ärakirjaga", "allkirjaga"],
                "answer": "allkirjaga"
            },
            {
                "question": "Palun tass musta _______.",
                "options": ["kohv", "kohvi", "kohvit"],
                "answer": "kohvi"
            },
            {
                "question": "Ilm oli külm ja puhus _______ tuul.",
                "options": ["järsk", "tugev", "kange"],
                "answer": "tugev"
            },
            {
                "question": "A: Kas sa oled tuludeklaratsiooni juba ära esitanud? B: _______.",
                "options": ["Veel mitte.", "Enam mitte.", "Miks ka mitte."],
                "answer": "Veel mitte."
            },
            {
                "question": "A: _______ sa trennis käid? B: Kord nädalas.",
                "options": ["Kui palju", "Kui tihti", "Kui kaua"],
                "answer": "Kui tihti"
            },
            {
                "question": "Suviti õpilasmalevas _______ õppisin hästi inimesi tundma.",
                "options": ["töötades", "töödates", "töötates"],
                "answer": "töötades"
            },
            {
                "question": "Apelsin on allergiat _______ puuvili.",
                "options": ["tekkiv", "tekitav", "tekitatav"],
                "answer": "tekitav"
            },
            {
                "question": "Ma ei tellinud kohvi, _______ teed!",
                "options": ["aga", "kuid", "vaid"],
                "answer": "vaid"
            },
            {
                "question": "A: Kui tihti sa pead tööreisidel käima? B: _______.",
                "options": ["Aeg-ajalt.", "Enam-vähem.", "Võib-olla."],
                "answer": "Aeg-ajalt."
            },
            {
                "question": "Kust Sa pärit _______?",
                "options": ["tuled", "oled", "saad"],
                "answer": "oled"
            },
            {
                "question": "See mõte ei meeldi _______.",
                "options": ["mul", "mult", "mulle"],
                "answer": "mulle"
            },
            {
                "question": "A: Kas te avaksite akna? B: _______.",
                "options": ["Ei, aitäh. Praegu mitte.", "Jah, kui te olete nii lahke.", "Jah, kohe."],
                "answer": "Jah, kohe."
            },
            {
                "question": "A: Mul tekkis teilt ostetud rösteriga probleem. B: _______.",
                "options": ["Pole probleemi!", "Pole minu probleem!", "Milles probleem?"],
                "answer": "Milles probleem?"
            },
            {
                "question": "A: Tere, minu nimi on Mari. B: _______.",
                "options": ["Meeldiv tutvuda!", "Palju õnne!", "Kena päeva!"],
                "answer": "Meeldiv tutvuda!"
            },
            {
                "question": "A: Kas sa saaksid mulle 20 eurot laenata? B: _______.",
                "options": ["Mul pole kahjuks sularaha.", "Ma maksan sulle palgapäeval tagasi.", "Väga kahju!"],
                "answer": "Mul pole kahjuks sularaha."
            },
            {
                "question": "A: Atsihh! B: _______",
                "options": ["Jõudu!", "Aitäh!", "Terviseks!"],
                "answer": "Terviseks!"
            },
            {
                "question": "Õnnetuse _______ helistage numbrile 112.",
                "options": ["korral", "kallal", "tõttu"],
                "answer": "korral"
            },
            {
                "question": "Juuksur töötab _______.",
                "options": ["salongis", "postkontoris", "restoranis"],
                "answer": "salongis"
            },
            {
                "question": "Need raamatud sarnanevad üksteisega sisu _______.",
                "options": ["üle", "järgi", "poolest"],
                "answer": "poolest"
            },
            {
                "question": "Kas teie _______ uute töötajate koolitamise eest?",
                "options": ["vastate", "avastate", "vastutate"],
                "answer": "vastutate"
            },
            {
                "question": "Palun _______arvuti välja!",
                "options": ["keera", "pane", "lülita"],
                "answer": "lülita"
            },
            {
                "question": "A: Millal algab uus aasta? B: _______",
                "options": ["Esimene jaanuar.", "Esimesel jaanuaril.", "Esimest jaanuari."],
                "answer": "Esimesel jaanuaril."
            },
            {
                "question": "A: Saan ma sulle kuidagi kasulik olla? B: _______.",
                "options": ["Aitäh, aga ma saan ise hakkama.", "Tunne ennast nagu kodus.", "Pole viga!"],
                "answer": "Aitäh, aga ma saan ise hakkama."
            },
            {
                "question": "A: Vabandust, et teid tülitan. B: _______.",
                "options": ["Minu viga!", "Pole viga!", "Sulle ka!"],
                "answer": "Pole viga!"
            },
            {
                "question": "Ta ei _______ autoga sõita.",
                "options": ["oska", "oskab", "oskama"],
                "answer": "oska"
            },
            {
                "question": "Me elame _______.",
                "options": ["Eestimaas", "Eestil", "Eestis"],
                "answer": "Eestis"
            },
            {
                "question": "Väljas on külm – pane kindad _______!",
                "options": ["selga", "kätte", "jalga"],
                "answer": "kätte"
            },
            {
                "question": "A: Kas te oskate mulle öelda, kuidas ma raamatukogu juurde saan? B: _______.",
                "options": ["Ma just ise tulen sealt.", "Kahjuks ei ole ma kohalik.", "Kesklinnas."],
                "answer": "Kahjuks ei ole ma kohalik."
            },
            {
                "question": "Tema ettepanek oli _______.",
                "options": ["asjalikuim", "asjalikeim", "asjalikem"],
                "answer": "asjalikem"
            },
            {
                "question": "A: Suutsin ma teid vastupidises veenda? B: _______.",
                "options": ["Kas ma võin teid hetkeks katkestada?", "Ma arvan, et jään oma seisukoha juurde.", "Ma sooviksin kellaaega täpsustada."],
                "answer": "Ma arvan, et jään oma seisukoha juurde."
            },
            {
                "question": "Kuulsin, et sul on homme eksam. Hoian sulle _______!",
                "options": ["sõrme", "kätt", "pöialt"],
                "answer": "pöialt"
            },
            {
                "question": "Palun _______ edasi, härra Peterson!",
                "options": ["astuksite", "astuge", "astu"],
                "answer": "astuge"
            },
            {
                "question": "Ta _______ hambaarstina.",
                "options": ["õpib", "on", "töötab"],
                "answer": "töötab"
            },
            {
                "question": "A: Oled sa näljane? B: _______",
                "options": ["Ei, ma just jõin.", "Ei, ma just sõin.", "Ei, mul on kõht tühi."],
                "answer": "Ei, ma just sõin."
            },
            {
                "question": "A: Hallo! Tere, palun Kallet. B: _______.",
                "options": ["Ma kuulen.", "Ma räägin.", "Ma ütlen."],
                "answer": "Ma kuulen."
            },
            {
                "question": "Päev pärast tänast on _______.",
                "options": ["eile", "homme", "ülehomme"],
                "answer": "ülehomme"
            },
            {
                "question": "Toas on kaks _______.",
                "options": ["tüdrukuid", "tüdrukud", "tüdrukut"],
                "answer": "tüdrukut"
            },
            {
                "question": "Ma armastan kinos _______.",
                "options": ["käima", "käin", "käia"],
                "answer": "käia"
            },
            {
                "question": "Õnnestunud naljade peale _______ publik kõva häälega.",
                "options": ["naerutab", "naeratab", "naerab"],
                "answer": "naerab"
            },
            {
                "question": "Kontor on avatud _______.",
                "options": ["kümnelt viieni", "kümnest viieni", "kümnest viiele"],
                "answer": "kümnest viieni"
            },
            {
                "question": "A: Vaatasin nädalavahetusel äärmiselt põnevat vestlussaadet. B: _______.",
                "options": ["Kui kahju!", "Väga tubli!", "Räägi lähemalt!"],
                "answer": "Räägi lähemalt!"
            },
            {
                "question": "Selles rahvamassis ei pääse ei edasi _______ tagasi.",
                "options": ["või", "ega", "ja"],
                "answer": "ega"
            },
            {
                "question": "Uues seiklusfilmis _______ lisaks näitlejatele ka üks tuntud poliitik.",
                "options": ["mängiv", "mängivat", "mängitavat"],
                "answer": "mängivat"
            },
            {
                "question": "Eelistan _______ roogi.",
                "options": ["vürtsikasi", "vürtsikaseid", "vürtsikaid"],
                "answer": "vürtsikaid"
            },
            {
                "question": "Mul kurk kuivab – kas ma saaksin natuke _______?",
                "options": ["vesi", "vee", "vett"],
                "answer": "vett"
            },
            {
                "question": "Kui nemad saabusid, oli meil juba _____.",
                "options": ["söönud", "söödud", "sõime"],
                "answer": "söödud"
            },
            {
                "question": "Palun _______ mulle seda punase rihmaga käekella!",
                "options": ["vaadake", "nähke", "näidake"],
                "answer": "näidake"
            },
            {
                "question": "A: Teeks õige nädalavahetusel ühe väljasõidu! B: _______.",
                "options": ["Mina ka mitte.", "Üsna hästi.", "Miks ka mitte."],
                "answer": "Miks ka mitte."
            },
            {
                "question": "A: Vabandage, kas ma tohin siia istuda? B: _______.",
                "options": ["Olge lahke.", "Heameelega.", "Kahjuks ma ei saa."],
                "answer": "Olge lahke."
            },
            {
                "question": "Kui ma oleks teadnud, mis kell on, siis ma _______.",
                "options": ["ei hiline", "ei hilinenud", "ei oleks hilinenud"],
                "answer": "ei oleks hilinenud"
            },
            {
                "question": "Tere _______, hea televaataja, kell on 13.00 ja algab AK.",
                "options": ["hommikust", "päevast", "õhtust"],
                "answer": "päevast"
            },
            {
                "question": "Eelmisel esmaspäeval jäi meil eesti keele tund _______.",
                "options": ["järele", "ära", "välja"],
                "answer": "ära"
            },
            {
                "question": "A: Läheks õige kinno. B: _______.",
                "options": ["Sul on õigus!", "Hea mõte!", "Hea, et niigi läks!"],
                "answer": "Hea mõte!"
            },
            {
                "question": "_______ sa Tartusse tagasi jõudsid?",
                "options": ["Kuna", "Kunas", "Kuni"],
                "answer": "Kuna"
            },
            {
                "question": "A: Kas sa saaksid mind aidata? B: _______.",
                "options": ["Väga tubli!", "Mis sa nüüd!", "Üks hetk!"],
                "answer": "Üks hetk!"
            },
            {
                "question": "A: Kena päeva jätku! B: _______.",
                "options": ["Vahet pole!", "Mis parata!", "Teile ka!"],
                "answer": "Teile ka!"
            },
            {
                "question": "A: Vabandage, mis kell on? B: _______.",
                "options": ["Pole tänu väärt!", "Oi, ma jään hiljaks!", "Kahjuks mul ei ole kella."],
                "answer": "Kahjuks mul ei ole kella."
            },
            {
                "question": "On väga _______, et me õigeks ajaks kohale jõuame.",
                "options": ["kahtlev", "kahtlustav", "kahtlane"],
                "answer": "kahtlane"
            },
            {
                "question": "A: Mul on täna sünnipäev. B: _______",
                "options": ["Tunnen kaasa!", "Palju edu!", "Palju õnne!"],
                "answer": "Palju õnne!"
            },
            {
                "question": "A: Kas te tšekki soovite? B: _______.",
                "options": ["Ei, ma maksan sularahas.", "Ei, aitäh.", "Ei, kahjuks mitte."],
                "answer": "Ei, aitäh."
            },
            {
                "question": "Kas sa võiksid _______ koti eest ära võtta?",
                "options": ["oma", "endi", "sinu"],
                "answer": "oma"
            },
            {
                "question": "A: Kas see pluus on teile paras? B: _______.",
                "options": ["Kus teil proovikabiinid asuvad?", "Kas teil saab kaardiga maksta?", "Kas ma võiksin igaks juhuks number suuremat proovida?"],
                "answer": "Kas ma võiksin igaks juhuks number suuremat proovida?"
            },
            {
                "question": "Ta helistas arstile ja sai aja _______ järgmiseks kolmapäevaks.",
                "options": ["ainult", "vaid", "alles"],
                "answer": "alles"
            },
            {
                "question": "See kleit sobib sulle _______.",
                "options": ["väga hea", "hea", "hästi"],
                "answer": "hästi"
            },
            {
                "question": "Me olime sunnitud koosoleku _______.",
                "options": ["edasi lükkama", "tagasi lükkama", "ümber lükkama"],
                "answer": "edasi lükkama"
            },
            {
                "question": "Räägitakse, et ta valdab _______.",
                "options": ["kuus võõrkeelt", "kuut võõrkeelt", "kuus võõrkeeli"],
                "answer": "kuut võõrkeelt"
            },
            {
                "question": "A: Jõudu! B: _______",
                "options": ["Tarvis.", "Palun.", "Terviseks."],
                "answer": "Tarvis."
            },
            {
                "question": "Loen praegu väga _______.",
                "options": ["huvitavat raamatut", "huvitav raamat", "huvitava raamatu"],
                "answer": "huvitavat raamatut"
            },
            {
                "question": "Just selline töö – hea palk, lühike tööpäev – on mulle _______.",
                "options": ["meelepärane", "sünnipärane", "omapärane"],
                "answer": "meelepärane"
            },
            {
                "question": "Peipsi rannad on tuntud kaunite luidete _______.",
                "options": ["järele", "poolest", "eest"],
                "answer": "poolest"
            },
            {
                "question": "Mul oli eile sünnipäev. Ma _______ palju kingitusi.",
                "options": ["saan", "saatsin", "sain"],
                "answer": "sain"
            },
            {
                "question": "Hea küll, ma võtan _______ pruunid saapad.",
                "options": ["see", "nad", "need"],
                "answer": "need"
            },
            {
                "question": "Olge tähelepanelikud ja hoidke _______ lahti.",
                "options": ["silmad-kõrvad", "käed-jalad", "sõrmed-varbad"],
                "answer": "silmad-kõrvad"
            },
            {
                "question": "A: Head reisi! B: _______.",
                "options": ["Pole viga!", "Head isu!", "Aitäh!"],
                "answer": "Aitäh!"
            },
            {
                "question": "Võta enne teele asumist midagi _______ alla!",
                "options": ["nina", "lõua", "hamba"],
                "answer": "hamba"
            },
            {
                "question": "A: Tere, doktor Tamm. Kas tohib? B: Jaa, palun astuge _______.",
                "options": ["välja", "läbi", "sisse"],
                "answer": "sisse"
            },
            {
                "question": "A: Mis on teie amet? B: _______.",
                "options": ["Ma olen abielus.", "Ma töötan kontoris.", "Ma olen politseinik."],
                "answer": "Ma olen politseinik."
            },
            {
                "question": "A: Mille üle te kaebate? B: _______.",
                "options": ["Kes oleks osanud arvata!", "Pole põhjust!", "Mind vaevab unetus."],
                "answer": "Mind vaevab unetus."
            },
            {
                "question": "Täna oli _______ väga palju rahvast.",
                "options": ["bussi", "bussis", "bussil"],
                "answer": "bussis"
            },
            {
                "question": "A: Aitäh abi eest! B: _______.",
                "options": ["Tühiasi.", "See polnud seda väärt.", "Ma ei saa sind aidata."],
                "answer": "Tühiasi."
            },
            {
                "question": "Õhtul on õues _______.",
                "options": ["tume", "pime", "must"],
                "answer": "pime"
            },
            {
                "question": "Seitsmekümnendatel kanti _______ pükse.",
                "options": ["laie", "laiu", "laia"],
                "answer": "laiu"
            },
            {
                "question": "A: Olete te valmis tellima? B: _______.",
                "options": ["See on kõik.", "Jaa, palun üks puuviljatee.", "Ma ei söö liha."],
                "answer": "Jaa, palun üks puuviljatee."
            },
            {
                "question": "Püüdke säilitada _______!",
                "options": ["külma aru", "külma meelt", "külma närvi"],
                "answer": "külma närvi"
            },
            {
                "question": "Siin on nii pime. Ma panen _______ põlema.",
                "options": ["tule", "tuli", "tuld"],
                "answer": "tule"
            },
            {
                "question": "Palun ära sellest _______ räägi!",
                "options": ["kellegile", "kellelegi", "kellegi"],
                "answer": "kellelegi"
            },
            {
                "question": "A: Kahjuks on ta hetkel hõivatud. B: _______.",
                "options": ["Kas te võiksite talle midagi edasi öelda?", "Kas ma saan talle midagi edasi öelda?", "Äkki saan mina kuidagi aidata?"],
                "answer": "Kas te võiksite talle midagi edasi öelda?"
            },
            {
                "question": "A: Kuidas oleks ühe kohviga? B: _______.",
                "options": ["Hea mõte!", "Aga teile?", "Pole hullu!"],
                "answer": "Hea mõte!"
            },
            {
                "question": "Vaikne muusika aitab _______.",
                "options": ["pingeid maandada", "pingeid muundada", "pingeid maanduda"],
                "answer": "pingeid maandada"
            },
            {
                "question": "_______ te lähete?",
                "options": ["Kus", "Kuhu", "Kust"],
                "answer": "Kuhu"
            },
            {
                "question": "Soovitan teil enne tööintervjuud hästi _______.",
                "options": ["ette valmistuda", "ette valmistada", "valmis vormistada"],
                "answer": "ette valmistuda"
            },
            {
                "question": "Ma _______ iga päev tööl.",
                "options": ["lähen", "tulen", "käin"],
                "answer": "käin"
            },
            {
                "question": "A: Kuidas läheb? B: _______",
                "options": ["Aitäh.", "Palun.", "Päris hästi."],
                "answer": "Päris hästi."
            },
            {
                "question": "Ta _______ mulle tere.",
                "options": ["rääkis", "jutustas", "ütles"],
                "answer": "ütles"
            },
            {
                "question": "A: Kas te räägite soome keelt? B: _______.",
                "options": ["Jah, ma räägin rootsi keelt.", "Ma saan aru, aga ei räägi.", "Ma olen sündinud Saaremaal."],
                "answer": "Ma saan aru, aga ei räägi."
            }
        ]
        self.create_widgets()

    def create_widgets(self):
        self.frame_top = tk.Frame(self.root, pady=10, padx=10)
        self.frame_top.pack(fill="x")
        self.title_label = tk.Label(self.frame_top, text="Эстонский тест A2-С1 уровня", font=("Helvetica", 16))
        self.title_label.pack()

        self.frame_questions = tk.Frame(self.root, pady=10, padx=10)
        self.frame_questions.pack(fill="x")

        self.question_label = tk.Label(self.frame_questions, text="")
        self.question_label.pack(anchor="w")

        self.var = tk.StringVar()

        self.option_buttons = []
        for i in range(3):
            option_button = tk.Radiobutton(self.frame_questions, text="", variable=self.var, value="")
            self.option_buttons.append(option_button)

        self.next_button = tk.Button(self.root, text="Следующий вопрос", command=self.next_question)
        self.next_button.pack()

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            self.var.set("")
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option, value=option)
                self.option_buttons[i].pack(anchor="w")
        else:
            self.show_result()

    def next_question(self):
        answer = self.var.get()
        self.answers.append(answer)
        if answer == self.questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1
        self.display_question()

    def show_result(self):
        results_path = os.path.join(os.path.dirname(__file__), 'results.txt')
        with open(results_path, 'w', encoding='utf-8') as f:
            f.write(f'{self.score}\n')
            f.write(f'{len(self.questions)}\n')
            for answer in self.answers:
                f.write(f'{answer}\n')
            for question in self.questions:
                f.write(f'{question["answer"]}\n')

        self.root.destroy()

        subprocess.Popen(["python", "show_score.py"])

root = tk.Tk()
app = EstonianTestApp(root)
root.mainloop()
