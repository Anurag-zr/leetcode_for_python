class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split(".");
        arr2 = version2.split(".");

        maxLen = max(len(arr1),len(arr2))

        for i in range(0,maxLen):            
            if(i == len(arr1)):
                j=i
                while(j<len(arr2)):
                    if(int(arr2[j])>0): return -1
                    j+=1
                return 0;

            if i== len(arr2):
                j=i
                while(j<len(arr1)):
                    if(int(arr1[j])>0): return 1
                    j+=1

                return 0;   

            ver1 = int(arr1[i])
            ver2 = int(arr2[i])

            if(ver1>ver2): return 1
            if(ver2>ver1): return -1

        ver1 = int(arr1[i])
        ver2 = int(arr2[i])

        if(ver1>ver2): return 1
        if(ver2>ver1): return -1
        return 0