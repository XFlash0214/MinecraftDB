from firebase import firebase as fb

class FirebaseManager:
    app=fb.FirebaseApplication("https://piratedb-0214.firebaseio.com/")
    def wrotetofile(self, idnum, obj):
        result=self.app.put("",idnum,obj)

    def getallpirates(self):
        d=self.app.get("",None)
        return d
