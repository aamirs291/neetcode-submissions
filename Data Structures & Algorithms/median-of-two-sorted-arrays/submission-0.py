class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #binary search needs to be done on the smaller array
        #for our calculations we are assuming nums1 to be the smaller array. 
        #if it is bigger then we swap nums2 with nums1
            if len(nums1)>len(nums2):
                nums1, nums2 = nums2, nums1

            N = len(nums1)
            M = len(nums2)
            tot_size = N+M
            mid = (N+M)//2

            l = 0 
            r = N #we are doing binary search on the smaller array

            while l<=r:
                mid1 = l + (r-l)//2
                mid2 = mid - mid1

                l1 = float("-inf") if mid1==0 else nums1[mid1-1] #mid1-1 would be one pos before the partition
                l2 = float("-inf") if mid2==0 else nums2[mid2-1]
                r1 = float("inf") if mid1==N else nums1[mid1]#mid1 would already be at the correct pos in terms of idx
                r2 = float("inf") if mid2==M else nums2[mid2]


                if l1>r2:
                    r = mid1-1 #since our main calculation is being done on mid1 we can focus on chaging the pointer for this only
                               #mid2 = mid-mid1 would handle mid2's position
                               #size of first array is decreasing here & due to mid2 = mid-mid1 calc the size of 2nd array would increase due to
                               #equilibrium i.e. for the total size//2 on the left side there will be size//2 elements including first and second arrays
                elif l2>r1:
                    l = mid1+1 #same point as above; we are focusing on mid1 so when r1 is lesser than l2
                               # it means that r1's correct pos should be on the left side of the mid and that the partition should be made after the current mid postion
                               #i.e. there is no way we can partition to the left of mid and get the correct answer so we move l to mid1+1
                                #size of first array is increasing here & due to mid2 = mid-mid1 calc the size of 2nd array would decrease due to
                               #equilibrium i.e. for the total size//2 on the left side there will be size//2 elements including first and second arrays
                else:
                    return (max(l1,l2)+min(r1,r2))/2 if tot_size%2==0 else min(r1, r2)

                    #since we have taken m+n//2 initially if m+n was even then mid would equally divide the left and right portions. But if
                    #it was odd then the right portion would have one extra element which is why we haev to do min(r1,r2)