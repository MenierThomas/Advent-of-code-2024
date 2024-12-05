fd = "str.txt"

def is_correctly_ordered(update, order_relation):
    for i in range(len(update)):
        priority_over = [second for first, second in order_relation if first == update[i]]
        for j in range(i):
            if update[j] in priority_over:
                return False
    return True

def main():    
    order_relation = []
    elf_sum = 0
    with open(fd, 'r') as file:
        content = file.read()
        ordering_rules, updates = content.split("\n\n")

        for line in ordering_rules.split("\n"):
            a, b = line.split('|')
            order_relation.append((a, b))

        for update_chains in updates.split("\n"):
            update = update_chains.split(',')
            if is_correctly_ordered(update, order_relation):
                elf_sum += int(update[len(update)//2])                 
    print(elf_sum)            


if __name__ == "__main__":
    main()
