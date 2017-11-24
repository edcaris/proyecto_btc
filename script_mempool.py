from subprocess import call
from subprocess import check_output
import time
import json

# Antes de ejecutar el script, iniciar "bitcoind -daemon" en la terminal.

folderName = "{}".format(int(time.time()))

# Se crea un nuevo directorio para guardar datos mempool:
call(["mkdir", "/home/ed/Documents/proyecto_btc/mempooldumps/{}".format(folderName)])

startTime = time.time()
currTime = startTime
blockCount = 0
numBlocks = -1

while True:

    # Tiempo de ejecucion:
    tActual = int(time.time() - startTime)
    print("\n\n" + 34*"-")
    hh = tActual // 3600
    mm = (tActual % 3600) // 60
    ss = tActual % 60
    print("Runtime (hhh:mm:ss):\t{:03.0f}:{:02.0f}:{:02.0f}".format(hh,mm,ss))
    mmc = (time.time() - currTime) // 60
    ssc = (time.time() - currTime) % 60
    print("Blocktime (mmm:ss):\t   {:03.0f}:{:02.0f}".format(mmc, ssc))


    # Actualiza numero de bloques:
    call(["bitcoin-cli", "getblockcount"])
    newBlockCount = int(check_output(["bitcoin-cli", "getblockcount"]))


    # Actualizar mempool dump:
    mempool = check_output(["bitcoin-cli", "getrawmempool"]).decode("utf-8")
    with open("./mempooldumps/{}/mp{}.txt".format(folderName, newBlockCount+1), "w") as mempool_file:
        mempool_file.write("Time={}\nnBlock={}\n{}".format(time.time(), newBlockCount+1, mempool))
    mempoolinfo = check_output(["bitcoin-cli", "getmempoolinfo"]).decode("utf-8")
    mempoolinfo_json = json.loads(mempoolinfo)
    mempoolnumtx = mempoolinfo_json["size"]

    # Detecta si hay un nuevo bloque:
    if newBlockCount != blockCount:
        numBlocks += 1
        currTime = time.time()
    blockCount = newBlockCount


    # Imprime informacion:
    print("Altura de blockchain:\t   {}".format(blockCount))
    print("Bloques validados:\t        {}".format(numBlocks))
    print("Numero de Tx's:\t\t    {}".format(mempoolnumtx))
    time.sleep(1)
