# -*- coding: utf-8 -*-
import LineAlpha
from LineAlpha.Gen.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LineAlpha.LINE()
cl.login(token="EoFyTN5cuZusJzlrvi82.WCCRkMNgQXINSOQNF/5yiG.YNh0Cv1TdVqgkNEbIvsgeRJNa99LJD9CeieE+vum3PM=")
cl.loginResult()

kk =  LineAlpha.LINE()
kk.login(token="EoxYKsNvY1B8LGmkVmZf.iC4lfEriEzKXeWEY6lQf+W.jPgs92NtejVbVNRBYPWAqb+b3OxLZKRVEsk/GrRBnc4=")
kk.loginResult()

ki =  LineAlpha.LINE()
ki.login(token="EolJosq08pRjFvdh01Lf.AzOxSrYUoRO+s8R0wGFDNW.yGYmJgiM7hMnqWkvSVxrEHVEXl/H2yZrIXHE5dH4gFM=")
ki.loginResult()

kc =  LineAlpha.LINE()
kc.login(token="EofFZlsuecjWl46bsXT2.zz02fzUHgHMt43YFBMIUuG.KFi7Vp0D6myIy07SnjtKIcWBNiOKDM63eJXGcANjN6g=")
kc.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""❧[Auto leave:on/off]
❧[Mid [@TAGORG]]
❧[Set group]
❧[Banned [@]]
❧[Unban [@]]
❧[Kill [@]]
❧[Invite mid]
❧[Spamcontact [@]]
❧[Admin add [@]]]
❧[Albumat']
❧[random: [JUMLAH]]
❧[Admin remove [@]]
❧[Bc [TEKS]]
❧[Group bc [TEKS]]
❧[Contact bc [TEKS]]
✍️T̸̡̛̎ͬͩ̀̂̿́́̾͌̃̋̀́̚͟͜Σ̸̸̲͔̲͖̞̈͑ͦͬ̈ͫ̈́̈́̐̾ͣ́̒Δ̣̰͆͢͡͞M̸̨̧̉́͘͢ ̢̠̮̰̼̈͒̋̊͆̌̐̌ͫ̂ͧ͋ͭͪ̈́͜J̠͂̽̂̏̄͆̌̐̎̾Ω̷̨̨̖̘̹ͬ́́͢͞Ҝ̛̭ͯ͌͒ͭͨ̂̏̔̚͝Σ̯͇̳͕͔ͩͣR̶̬͕̬̟̎ͩ̅͛̽ͤ̇̊ͧ͊͛̚̕͞҉̛̛͘͠͏̵ ̟̮̰̒̒ͣ̀̄̂̔͒̔͋̚͜͝͡β̴̨̛ͫͫ̄͊́̚Ω̫̈ͤ́̋ͩ͂̄̀ͥ͛ͥ̒̈́̇̚Ţ̵̸̸̡̛̲̩̐͛ͦ͌̃̓ͩ̃̏̓ͨ̄̓͆̀̕̕͞͞͠S̳̪̘̒̐̑ͧͦ͏̵̛̀̕͡͡ ✈
"""

Setgroup =""" GROUP PROTECTION
❧[Protect on/off]
❧[Contact on/off]
❧[Cancel on/off]
❧[Join on/off]
"""
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid]
admin=["uc1c72b2a69c6ab18a7b28aa77fee5822"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "UpdateName":True,
    "cName":"",
    "cName1":"✍️T̸̡̛̎ͬͩ̀̂̿́́̾͌̃̋̀́̚͟͜Σ̸̸̲͔̲͖̞̈͑ͦͬ̈ͫ̈́̈́̐̾ͣ́̒Δ̣̰͆͢͡͞M̸̨̧̉́͘͢ ̢̠̮̰̼̈͒̋̊͆̌̐̌ͫ̂ͧ͋ͭͪ̈́͜J̠͂̽̂̏̄͆̌̐̎̾Ω̷̨̨̖̘̹ͬ́́͢͞Ҝ̛̭ͯ͌͒ͭͨ̂̏̔̚͝Σ̯͇̳͕͔ͩͣR̶̬͕̬̟̎ͩ̅͛̽ͤ̇̊ͧ͊͛̚̕͞҉̛̛͘͠͏̵ ̟̮̰̒̒ͣ̀̄̂̔͒̔͋̚͜͝͡β̴̨̛ͫͫ̄͊́̚Ω̫̈ͤ́̋ͩ͂̄̀ͥ͛ͥ̒̈́̇̚Ţ̵̸̸̡̛̲̩̐͛ͦ͌̃̓ͩ̃̏̓ͨ̄̓͆̀̕̕͞͞͠S̳̪̘̒̐̑ͧͦ͏̵̛̀̕͡͡ ✈",
    "cName2":"✍️T̸̡̛̎ͬͩ̀̂̿́́̾͌̃̋̀́̚͟͜Σ̸̸̲͔̲͖̞̈͑ͦͬ̈ͫ̈́̈́̐̾ͣ́̒Δ̣̰͆͢͡͞M̸̨̧̉́͘͢ ̢̠̮̰̼̈͒̋̊͆̌̐̌ͫ̂ͧ͋ͭͪ̈́͜J̠͂̽̂̏̄͆̌̐̎̾Ω̷̨̨̖̘̹ͬ́́͢͞Ҝ̛̭ͯ͌͒ͭͨ̂̏̔̚͝Σ̯͇̳͕͔ͩͣR̶̬͕̬̟̎ͩ̅͛̽ͤ̇̊ͧ͊͛̚̕͞҉̛̛͘͠͏̵ ̟̮̰̒̒ͣ̀̄̂̔͒̔͋̚͜͝͡β̴̨̛ͫͫ̄͊́̚Ω̫̈ͤ́̋ͩ͂̄̀ͥ͛ͥ̒̈́̇̚Ţ̵̸̸̡̛̲̩̐͛ͦ͌̃̓ͩ̃̏̓ͨ̄̓͆̀̕̕͞͞͠S̳̪̘̒̐̑ͧͦ͏̵̛̀̕͡͡ ✈",
    "cName3":"􀀷􀰂􀰂꧁Kicker꧂􏿿􀀷",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    'copy':True,
    'target':{},
    'midsTarget':{},
}

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile() 
backup = cl.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
		
        #------Protect Group Kick start------#
        if op.type == 11:
           if wait["Protectgr"] == True:
               if op.param2 not in Bots:
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  Ticket = ki.reissueGroupTicket(op.param1)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ku.kickoutFromGroup(op.param1,[op,param2])
                  ki.updateGroup(G)
                  ku.leaveGroup(op.param1)
        #------Protect Group Kick finish-----#
        #------CCTV-------------===----------#
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass

        #-----------------------------------#
		
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
            elif "Sangein " in msg.text:
              if msg.from_ in admin:
                sangein0 = msg.text.replace("Sangein ","")
                sangein1 = sangein0.rstrip()
                sangein2 = sangein1.replace("@","")
                sangein3 = sangein2.rstrip()
                _name = sangein3
                gs = ki.getGroup(msg.to)
                ginfo = ki.getGroup(msg.to)
                gs.preventJoinByTicket = False
                ki.updateGroup(gs)
                invsend = 0
                Ticket = ki.reissueGroupTicket(msg.to)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        kc.kickoutFromGroup(msg.to,[target])
                                        kc.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        kc.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        ki.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        ki.updateGroup(gs)
            elif msg.text is None:
                return
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif "Kick " in msg.text:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Cv1 kick " in msg.text:
                midd = msg.text.replace("Cv1 kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Cv2 kick " in msg.text:
                midd = msg.text.replace("Cv2 kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Cv3 kick " in msg.text:
                midd = msg.text.replace("Cv3 kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Cv1 invite " in msg.text:
                midd = msg.text.replace("Cv1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Cv2 invite " in msg.text:
                midd = msg.text.replace("Cv2 invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Cv3 invite " in msg.text:
                midd = msg.text.replace("Cv3 invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["Cv1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
		
            elif "copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.cloneContactProfile(target)
                               cl.sendText(msg.to, "Suksesclone...")
                            except Exception as e:
                                print e
                                
            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to, "Suksesbackup...")
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
			
            elif msg.text in ["cancel","Cancel"]:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                    else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Gurl"]:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Y"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        G = kk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                        print "All complete"
                        G.preventJoinByTicket(G)
                        kk.updateGroup(G)
#------------------------------------------------------------#
    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["O"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        cl.sendText(msg.to,"Sudah keluar")
                    except:
                        pass
#-----------------------------------------------------#
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Summon"]:
              if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Cv1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Cv2 mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "Cv3 mid" == msg.text:
                kc.sendText(msg.to,Cmid)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set group"]:
                md = ""
                if wait["contact"] == True: md+=" Contact : off\n"
                else: md+=" Contact : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave : off\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share : off\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : off\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : off\n"
                else:md+=" Comment : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif msg.text in ["Set"]:
                    cl.sendText(msg.to, "Check")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "set point"
                    
            elif msg.text == "Lurking":
                    cl.sendText(msg.to, "Set reading point:" + datetime.today().strftime('\n%Y-%m-%d %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text == "Sider":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "==============================\nActive readers:%s\n\n\n\nPassive readers:\n%s\n\n==============================\nIn the last seen point:\n[%s]\n==============================\n [?]Powered By: ✍️T̸̡̛̎ͬͩ̀̂̿́́̾͌̃̋̀́̚͟͜Σ̸̸̲͔̲͖̞̈͑ͦͬ̈ͫ̈́̈́̐̾ͣ́̒Δ̣̰͆͢͡͞M̸̨̧̉́͘͢ ̢̠̮̰̼̈͒̋̊͆̌̐̌ͫ̂ͧ͋ͭͪ̈́͜J̠͂̽̂̏̄͆̌̐̎̾Ω̷̨̨̖̘̹ͬ́́͢͞Ҝ̛̭ͯ͌͒ͭͨ̂̏̔̚͝Σ̯͇̳͕͔ͩͣR̶̬͕̬̟̎ͩ̅͛̽ͤ̇̊ͧ͊͛̚̕͞҉̛̛͘͠͏̵ ̟̮̰̒̒ͣ̀̄̂̔͒̔͋̚͜͝͡β̴̨̛ͫͫ̄͊́̚Ω̫̈ͤ́̋ͩ͂̄̀ͥ͛ͥ̒̈́̇̚Ţ̵̸̸̡̛̲̩̐͛ͦ͌̃̓ͩ̃̏̓ͨ̄̓͆̀̕̕͞͞͠S̳̪̘̒̐̑ͧͦ͏̵̛̀̕͡͡ ✈" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Auto set reading point in:" + datetime.datetime.today().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "Reading point has not been set.")
#-----------------------------------------------
#----------------Commandtambahan----------------------#
            elif msg.text in ["List group","Glist"]:
              if msg.from_ in admin:
               gid = cl.getGroupIdsJoined()
               h = ""
               for i in gid:
                h += "[⭐] %s  \n" % (cl.getGroup(i).name + " | Members : " + str(len (cl.getGroup(i).members)))
               cl.sendText(msg.to, "☆「Group List」☆\n"+ h +"Total Group : " +str(len(gid)))
               
            elif msg.text in ["Creator"]:
                      msg.contentType = 13
                      Creatorbot = "uc1c72b2a69c6ab18a7b28aa77fee5822"
                      try:
                          msg.contentMetadata = {'mid': Creatorbot}
                        
                      except:
                        Creatorbot = "Error"
                      cl.sendText(msg.to, "🅂🅄🄿🄿🄾🅁🅃 🄱🅈 ✍️T̸̡̛̎ͬͩ̀̂̿́́̾͌̃̋̀́̚͟͜Σ̸̸̲͔̲͖̞̈͑ͦͬ̈ͫ̈́̈́̐̾ͣ́̒Δ̣̰͆͢͡͞M̸̨̧̉́͘͢ ̢̠̮̰̼̈͒̋̊͆̌̐̌ͫ̂ͧ͋ͭͪ̈́͜J̠͂̽̂̏̄͆̌̐̎̾Ω̷̨̨̖̘̹ͬ́́͢͞Ҝ̛̭ͯ͌͒ͭͨ̂̏̔̚͝Σ̯͇̳͕͔ͩͣR̶̬͕̬̟̎ͩ̅͛̽ͤ̇̊ͧ͊͛̚̕͞҉̛̛͘͠͏̵ ̟̮̰̒̒ͣ̀̄̂̔͒̔͋̚͜͝͡β̴̨̛ͫͫ̄͊́̚Ω̫̈ͤ́̋ͩ͂̄̀ͥ͛ͥ̒̈́̇̚Ţ̵̸̸̡̛̲̩̐͛ͦ͌̃̓ͩ̃̏̓ͨ̄̓͆̀̕̕͞͞͠S̳̪̘̒̐̑ͧͦ͏̵̛̀̕͡͡ ✈")
                      cl.sendMessage(msg)
#-----------------------------------------------

#-----------------------------------------------
#-----------------------------------------------

#-----------------------------------------------
            elif msg.text in ["Kill"]:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Fuck You")
                        kc.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    cl.sendText(msg.to,"Just some casual cleansing ô")
                    cl.sendText(msg.to,"Group cleansed.")
                    cl.sendText(msg.to,"Fuck You All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group cleanse")
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes ")
                                    kk.sendText(msg.to,"Fuck You")
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes Cv")
                                except:
                                    ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found ")
                        kk.sendText(msg.to,"Not found ")
                        kc.sendText(msg.to,"Not found ")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes ")
                                ki.sendText(msg.to,"Succes ")
                                kk.sendText(msg.to,"Succes ")
                            except:
                                ki.sendText(msg.to,"Error")
                                kk.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found ")
                        kk.sendText(msg.to,"Not found ")
                        kc.sendText(msg.to,"Not found ")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes ")
                            except:
                                ki.sendText(msg.to,"Succes ")
#-----------------------------------------------

#-----------------------------------------------
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
#-----------------------------------------------

#------------------------------------------------------
            elif "Steal dp @" in msg.text:            
                   print "[Command]dp executing"
                   _name = msg.text.replace("Steal dp @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to,"Contact not found")
                   else:
                       for target in targets:
                           try:
                               contact = cl.getContact(target)
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               cl.sendImageWithURL(msg.to, path)
                           except:
                               pass
                   print "[Command]dp executed"]
#-----------------------------------------------------------
#------------------------------------------------- 
#-----------------------------------------------
#-----------------------------------------------

            elif "Spam " in msg.text:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   if txt[1] == "on":
                        if jmlh <= 1000:
                             for x in range(jmlh):
                               cl.sendText(msg.to,teks)
                   elif txt[1] == "off":
                         if jmlh <= 1000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
			
            elif "Group bc " in msg.text:
               bctxt = msg.text.replace("Group bc ", "")
               n = cl.getGroupIdsJoined()
               for manusia in n:
                  cl.sendText(manusia, (bctxt))
			
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)

       #--------------Fungsi Broadcast Finish-----------#
#-----------------------------------------------
            elif "Mid @" in msg.text: 
	      if msg.from_ in owner: 
		 _name = msg.text.replace("Mid @","") 
		 _nametarget = _name.rstrip(' ') 
 		 gs = cl.getGroup(msg.to) 
		 lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')} 
		 msg.contentMetadata = lol 
		 for g in gs.members: 
		 if _nametarget == g.displayName: 
		 random.choice(KAC).sendText(msg.to,"Mid:\n" + msg + g.mid) 
	      else: 
#-------------------------------------------------------
            elif 'XpertCrash' in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc1c72b2a69c6ab18a7b28aa77fee5822,'"}
                cl.sendText(msg.to,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")
                cl.sendMessage(msg)
#-------------------------------------------------------
#-------------------------------------------------------
            elif 'Crash' in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc1c72b2a69c6ab18a7b28aa77fee5822,'"}
                cl.sendMessage(msg)
#-------------------------------------------------------  
            elif msg.text in ["404"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Respon","respon"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"✍️T̸̡̛̎ͬͩ̀̂̿́́̾͌̃̋̀́̚͟͜Σ̸̸̲͔̲͖̞̈͑ͦͬ̈ͫ̈́̈́̐̾ͣ́̒Δ̣̰͆͢͡͞M̸̨̧̉́͘͢ ̢̠̮̰̼̈͒̋̊͆̌̐̌ͫ̂ͧ͋ͭͪ̈́͜J̠͂̽̂̏̄͆̌̐̎̾Ω̷̨̨̖̘̹ͬ́́͢͞Ҝ̛̭ͯ͌͒ͭͨ̂̏̔̚͝Σ̯͇̳͕͔ͩͣR̶̬͕̬̟̎ͩ̅͛̽ͤ̇̊ͧ͊͛̚̕͞҉̛̛͘͠͏̵ ̟̮̰̒̒ͣ̀̄̂̔͒̔͋̚͜͝͡β̴̨̛ͫͫ̄͊́̚Ω̫̈ͤ́̋ͩ͂̄̀ͥ͛ͥ̒̈́̇̚Ţ̵̸̸̡̛̲̩̐͛ͦ͌̃̓ͩ̃̏̓ͨ̄̓͆̀̕̕͞͞͠S̳̪̘̒̐̑ͧͦ͏̵̛̀̕͡͡ ✈")
                kk.sendText(msg.to,"✍️T̸̡̛̎ͬͩ̀̂̿́́̾͌̃̋̀́̚͟͜Σ̸̸̲͔̲͖̞̈͑ͦͬ̈ͫ̈́̈́̐̾ͣ́̒Δ̣̰͆͢͡͞M̸̨̧̉́͘͢ ̢̠̮̰̼̈͒̋̊͆̌̐̌ͫ̂ͧ͋ͭͪ̈́͜J̠͂̽̂̏̄͆̌̐̎̾Ω̷̨̨̖̘̹ͬ́́͢͞Ҝ̛̭ͯ͌͒ͭͨ̂̏̔̚͝Σ̯͇̳͕͔ͩͣR̶̬͕̬̟̎ͩ̅͛̽ͤ̇̊ͧ͊͛̚̕͞҉̛̛͘͠͏̵ ̟̮̰̒̒ͣ̀̄̂̔͒̔͋̚͜͝͡β̴̨̛ͫͫ̄͊́̚Ω̫̈ͤ́̋ͩ͂̄̀ͥ͛ͥ̒̈́̇̚Ţ̵̸̸̡̛̲̩̐͛ͦ͌̃̓ͩ̃̏̓ͨ̄̓͆̀̕̕͞͞͠S̳̪̘̒̐̑ͧͦ͏̵̛̀̕͡͡ ✈")
      #-------------Fungsi Respon Finish---------------------#

      #-------------Fungsi Balesan Respon Start---------------------#
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa jadi")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                
            elif msg.text in ["Quote","quote","quotes","Quotes"]:
                quote = ['Aku sayang kamu']
                psn = random.choice(quote)
                cl.sendText(msg.to,psn)

      #-------------Fungsi Balesan Respon Finish---------------------#
			
#-----------------------------------------------
#-----------------------------------------------
#------------------------------------------------------#
             elif msg.text in ["d"]:
              if msg.from_ in admin:
               if wait["UpdateName"] == True:
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile = ki.getProfile()
                profile.displayName = wait["cName2"]
                kk.updateProfile(profile)

                profile = kk.getProfile()
                profile.displayName = wait["cName3"]
                kk.updateProfile(profile)

                profile = kc.getProfile()
                profile.displayName = wait["cName4"]
                kc.updateProfile(profile)
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.toType F:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invite]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error
        
def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
	
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def sendImage(self, to_, path):
        M = Message(to=to_, text=None, contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True

def sendImage2(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self._client.sendMessage(M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["UpdateName"] == True:
                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
