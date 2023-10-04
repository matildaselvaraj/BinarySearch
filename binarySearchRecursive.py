
# Rekursiv binary search
def binarySearch(A, target, lo, hi):
    
    # Kolla om det aktuella intervallet mellan lo och hi är 1 eller mindre (basfallet)
    # Isåfall finns det bara ett index kvar som kan vara vårt target
    if lo + 1 >= hi:
        if A[lo] == target:     
            return lo   # Returnera lo om lo pekar på vårt target 
        return None     # Annars innehåller inte arrayen vårt target, isåfall returnerar vi None
    
    # Om det aktuella intervallet mellan lo och hi är större än 1
    mid = (lo + hi)//2      # Hitta mid som mitten mellan lo och hi avrundat ner till närmsta heltal
    if A[mid] > target:
        return binarySearch(A, target, lo, mid)     # om mitten av intervallet har för stort värde kollar vi på den lägra halvan av intervallet
    else:
        return binarySearch(A, target, mid, hi)     # annars kollar vi på övre halvan av intervallet 

# Test:
A = [2, 4, 5, 7, 8]
target = 7
x = binarySearch(A, target, 0, len(A))
print(x)
    
    
