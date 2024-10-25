def bowling():
    # score_historic = [[10], [3,7], [2,8], ...]
    score_historic = []

    def turn(f):
        pins = 10
        score = []

        print(f"\n Frame {f}: ")

        for i in range(1,3):
            print(f"\n Pinos restantes: {pins} \n")
            point = input(f"Quantos pontos você fez na jogada {i}? ")

            while True:
                try:
                    point = int(point)
                    
                    if point <= pins:
                        pins = pins - point
                        break
                    else: 
                        raise ValueError()
            
                except:
                    print("Informe um valor válido\n")
                    print(f"\n Pinos restantes: {pins} \n")
                    point = input(f"Quantos pontos você fez na jogada {i}? ")

            if point == 10:
                score.append(point)
                break
            else:
                score.append(point)
        
        return score
    
    def extra_play(plays:int):
        score = []

        print(f"\n Parabéns, você ganhou mais {plays} jogada(s) \n")

        for i in range(1, plays+1):

            point = input(f"Quantos pontos você fez na jogada {i}? ")
            while True:
                try:
                    point = int(point)
                    
                    if point <= 10:
                        score.append(point)
                        break
                    else: 
                        raise ValueError()
            
                except:
                    print("Informe um valor válido\n")
                    point = input(f"Quantos pontos você fez na jogada {i}? ")
            
        return score
    

    for frame in range(0, 10):

        score_historic.append(turn(frame+1))

        # se estivermos no último frame
        if frame == 9:

            # se um strike tiver sido feito no último frame, dê ao jogador mais 2 jogadas
            if len(score_historic[-1]) == 1:
                for s_point in extra_play(2):
                    score_historic[-1].append(s_point)
            
            # se um spare tiver sido feito no último frame, dê ao jogador mais 1 jogada
            elif sum(score_historic[-1]) == 10:
                score_historic[-1].append(extra_play(1)[0])

    
    
    # somando o Total de pontos do jogador 
    points_each_turn = []

    for turn_code in range(0, len(score_historic)):

        points_on_turn = []
        
        # se o frame foi um strike, some os 10 pontos da jogada atual +  a pontuação das duas próximas jogadas
        if score_historic[turn_code][0] == 10:
            
            # esse loop adiciona os pontos da jogada atual + os pontos da proximas 2 jogadas à points_on_turn
            added_elements = 0

            for i in range(turn_code, len(score_historic)):
                if added_elements >= 3: 
                    break
                for element in score_historic[i]:
                    if added_elements >=3:
                        break
                    else:
                        points_on_turn.append(element)
                        added_elements += 1
                
        else:
            # se o frame foi um spare, some 10 + pontuação da próxima jogada 
            if sum(score_historic[turn_code]) == 10:

                # esse loop adiciona os pontos da jogada atual + os pontos da proxima jogada à points_on_turn
                added_elements = 0

                for i in range(turn_code, len(score_historic)):
                    if added_elements >= 2: 
                        break
                    for element in score_historic[i]:
                        if added_elements >=2:
                            break
                        else:
                            points_on_turn.append(element)
                            added_elements += 1

            else:
                points_on_turn = score_historic[turn_code]
        

        points_each_turn.append(sum(points_on_turn))

    print(f"\n A sua pontuação total foi de {sum(points_each_turn)} pontos!!")
            

bowling()

