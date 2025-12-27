import random
import time

Playlists = ["Coolie","Leo","Vikram","Master","Jailer","Devara","Animal","Saalar","KGF","KOK","SS","Pushpa","Petta","Beast","Marco","OSTS","Sahoo","Psycho-Dark"]
print("Playlists-Songs Recommending Bot")

def menu():
    print("""1.Add Playlist
2.Del Playlist
3.Get Rec
4.Show all the Playlists
5.Exit""")
    
menu()

def add_del_playlists(choice):
    if choice == 1:
        add_playlist = input("Enter the Playlist name to add : ")
        Playlists.append(add_playlist)
        print(f"'{add_playlist}' Playlist added in Playlists")
        
    elif choice == 2:
        rem_playlist = input("Enter the Playlist name to remove it : ")
        if rem_playlist in Playlists:
            Playlists.remove(rem_playlist)
            print(f"'{rem_playlist}' playlist removed from the playlists")
        else:
            print("Enter a playlist which already exists in the Playlists to remove")

def rec_show_playlists(choice):
    if choice == 3:
        if Playlists!=[]:
            print(f"🎧 Recommended : {Playlists[0]}")
        else:
            print("Playlist is empty, add some before getting recs...")
        
    elif choice == 4:
        for i,playlist in enumerate(Playlists):
            print(f"{i+1} : {playlist}")
            time.sleep(0.1)
        
while True:
    while True:
        try:
            choice = int(input())
            break
        except ValueError:
            print()
            print("Enter an Integer")
            menu()

    if choice == 1 or choice == 2:
        add_del_playlists(choice)
    elif choice == 3 or choice == 4:
        rec_show_playlists(choice)
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Enter a valid input : ")
        menu()

    time.sleep(1)
    print()
    print("What to do next?")
    menu()
        
       

