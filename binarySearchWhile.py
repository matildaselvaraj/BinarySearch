
A = [1, 1, 1, 1, 1, 1, 2, 4, 5, 7, 8]
target = 2



def binarySearch(A, target):

    # Våra pointers startar i vardera ända av arrayen 
    lo = 0          # lo (eller low) startar längst till vänster 
    hi = len(A)     # hi (eller high) startar till höger om slutet på arrayen 

    # Så länge som det aktuella intervallet mellan lo och hi är större än 1
    while lo + 1 < hi:     
        mid = (lo + hi)//2      # mid är mittemellan lo och hi, avrundat neråt till närmsta heltal
        if A[mid] > target:     
            hi = mid            # om mitten av intervallet har för stora värden kollar vi på den lägra halvan av intervallet
        else:
            lo = mid            # annars tittar vi på den övre halvan av intervallet 
    
    # När vi kommer ut ut while-loopen har vi endast ett index kvar som kan innehålla vårt target (det som lo pekar på)

    if A[lo] == target: 
        return lo       # returnera lo om den pekar på vårt target
        
    return None         # om lo inte pekar på vårt target så finns inte vårt target med i listan, då returnerar vi None

x = binarySearch(A, target)
print(x)