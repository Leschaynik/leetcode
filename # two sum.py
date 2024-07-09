class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        '''
        #1.0
        # проблемы: 1. повторяющиеся вычисления; 2. может пропустить подхожящий элемент из-за второго если (см. тест 3)
        c=0
        for num1 in nums:
            if (target - c) in nums:
                if c!=nums.index(target - c):
                    return [c, nums.index(target - c)]
            c+=1
        '''
        '''
        #1.1  
        ind_num1=len(nums)-1
        for num1 in nums[::-1]:
            num2=target - num1
            if num2 in nums:
                ind_num2=nums.index(num2)
                if ind_num1!=ind_num2:
                    return [ind_num2, ind_num1]
            ind_num1-=1
        '''
        '''
        #2.0 оптимальное
        # проблема: код не работатал для случев, когда в тесте несколько отрицательных чисел или вторым числом является отрицательное ([10, -1], 9)
        # решение: добавил -1 в 53 строку. как именно это помогло не понял. - предположительно, так как длинна массива на 1 больше его максимального индека, -1 позволяет массиву длинной 2 делиться пополам правильно
        def binary_search(num, List):
            """
            in: num, List
            out: index or False (-1)
            """

            def search(num, s_List):
                #print('Q', num, s_List)
                if len(s_List)==1:
                    if s_List[0][0]==num:
                        #print(s_List[0][1])
                        return s_List[0][1]
                    else:
                        #print(False)
                        # -1, а не False, так как иначе будут проблемы с 0м индексом при проверкек ниже *
                        return -1
                    

                #print(s_List[len(s_List)//2])    
                if s_List[len(s_List)//2-1][0]<num:
                    return search(num, s_List[len(s_List)//2:])
                else:
                    return search(num, s_List[:len(s_List)//2])
                
            s_List=sorted([[List[i], i] for i in range(len(List))])
            
            return search(num, s_List)

        ind_num1=len(nums)-1
        #s_List=sorted([[nums[i], i] for i in range(len(nums))])

        # перебор от конца списка к началу чтобы небыло случая, когда мы в ответе берём один и тот же элемент два раза 
        for num1 in nums[::-1]:
            bin_in=binary_search(target - num1, nums)
            # проблема была бы тут *
            if bin_in>=0:
                    return [bin_in, ind_num1]
            ind_num1-=1
        '''
        '''
        #2.1
        def binary_search(num, List):
            """
            in: num, List
            out: index or False
            """
        
            def search(num, s_List):
                #print(num, s_List)
                if len(s_List)==1:
                    if s_List[0][0]==num:
                        # костыльная реализация задумки о возвращении False
                        return [True, s_List[0][1]]
                    else:
                        return [False, False]

                #print(s_List[len(s_List)//2])
                halflen_s_List=len(s_List)//2
                halfelem_s_List=s_List[halflen_s_List-1]
                if halfelem_s_List[0]<num:
                    return search(num, s_List[halflen_s_List:])
                else:
                    if halfelem_s_List[0]>num:
                        return search(num, s_List[:halflen_s_List])
                    else:
                        # попытка ускорить код при помощи проверки на то, что центральное число уже искомое
                        return [True, halfelem_s_List[1]]
                
            #s_List=sorted([[List[i], i] for i in range(len(List))])
            
            return search(num, s_List)

        ind_num1=0
        s_List=sorted([[nums[i], i] for i in range(len(nums))])

        for num1 in nums:
            bin_search=binary_search(target - num1, s_List)
            #более надёжный вариант с проверкой на наличие и на совпадение с уже взятым элементом
            if bin_search[0] and ind_num1!=bin_search[1]:
                    return [bin_search[1], ind_num1]
            ind_num1+=1
        '''
        ''' '''
        #1.3
        numdict=dict()

        for i in range(len(nums)):
            if target-nums[i] in numdict:
                return [numdict[target-nums[i]], i]
            numdict[nums[i]]==i

        return[] #если нет решения
    