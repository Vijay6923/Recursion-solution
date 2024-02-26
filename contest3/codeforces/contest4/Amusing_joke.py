def can_form_names(guest_name, host_name, pile_letters):
    full_names = guest_name + host_name
    return sorted(full_names) == sorted(pile_letters)


guest_name = input().strip()
host_name = input().strip()
pile_letters = input().strip()
if can_form_names(guest_name, host_name, pile_letters):
    print("YES")
else:
    print("NO")
