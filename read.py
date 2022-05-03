from display import displayData
# tip lng, macacall itong function everytime may sinelect na option sa filter combobox
def read(cursor, records):
    cursor = cnt.execute()
print(cursor)
for i in cursor:
    print(i[0]+"    "+str(i[1])+"   "+str(i[2]))

print('')
    #placeholder lng
    # para mapadali buhay mo, check mo code sa displayData function kung pano mag clear at insert ng rows sa table('records') ng app