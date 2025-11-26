def total_distance(leftList, rightList, distance = 0):
    for left, right in zip(leftList, rightList):
        if left > right:
            dist = left - right
            distance += dist
        elif right > left:
            dist = right - left
            distance += dist
        elif left == right:
            distance += 0
    return distance


def similarity_score(leftList, rightList, similarityScore = 0):
    for num in leftList:
        amt = rightList.count(num)
        similarityScore += num*amt
    return similarityScore

def main():
    with open('AdventOfCode\\day1.txt', 'r') as file:
        lines = file.readlines()

    leftList, rightList = [], []
    for line in lines:
        Split = line.split()
        leftList.append(int(Split[0]))
        rightList.append(int(Split[1]))

    leftList.sort()
    rightList.sort()

    distance = total_distance(leftList, rightList)
    similarity = similarity_score(leftList, rightList)
    
    print(f"Distance: {distance}")
    print(f"Similarity: {similarity}")

main()