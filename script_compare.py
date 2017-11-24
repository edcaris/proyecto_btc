from subprocess import call
from subprocess import check_output
import json


# asignar el # del bloque inicial
blocknum = 490000
blocknum2 = 490001

#call(["mkdir", "/home/ed/Documents/proyecto_btc/blockdumps/{}".format(folderName)])


for i in range(blocknum,blocknum2):

    Blockhash = (check_output(["bitcoin-cli", "getblockhash", "{}".format(i)]))
    Block = (check_output(["bitcoin-cli", "getblock","{}".format(Blockhash)]))
    blockinfo_json = json.loads(Block)
    txs = blockinfo_json["tx"]


    #print(txs[1])
