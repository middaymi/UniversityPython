# Goldobina Svetlana
#
# proportionally allocate seats in the parliament


def election(f):
    parties = {}
    all_voices = 0
    with open(f, 'r') as result:
        for line in result:
            party_list = line.strip().split(' ')
            # a dictionary with a party name and numbers of voices, then add places
            parties[party_list[1]] = dict(voices=int(party_list[2]))
            all_voices = all_voices + int(party_list[2])

    first_electoral_quotient = all_voices / 450
    summary_places = 0
    # count a number of places for each party
    for p in parties:
        places = parties[p]['voices'] // first_electoral_quotient
        parties[p]['places'] = places
        summary_places = summary_places + places

    if summary_places < 450:  # are there free places?
        # sort parties by places, start at the biggest values
        s_parties = sorted(parties, key=lambda item: parties[item]['places'], reverse=True)
        rest_places = 450 - summary_places
        while rest_places:  # divide free places
            for p in s_parties:
                s_parties = s_parties[1:]
                for np in s_parties:
                    if parties[p]['places'] > parties[np]['places']:  # at first who has the biggest value
                        parties[p]['places'] += 1
                        rest_places -= 1
                        break
                    elif parties[p]['places'] == parties[np]['places']:
                        if parties[p]['voices'] > parties[np]['voices']:
                            parties[p]['places'] += 1
                        else:
                            parties[np]['places'] += 1
                        rest_places -= 1
                        break
                break
    for k in parties:
        print("Party " + k + " " + str(int(parties[k]['places'])))


# start
election("files/result_election3")