def fizzbuzz(quy_tac):
    for so in range(1, 101):
        ket_qua = ""
        for so_chia in sorted(quy_tac.keys()):
            if so % so_chia == 0:
                ket_qua += quy_tac[so_chia]
        if ket_qua == "":
            print(so)
        else:
            print(ket_qua)

if __name__ == "__main__":
    luat_moi = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    fizzbuzz(luat_moi)