import streamlit as st


def find_combinations_summing_to_target(numbers, target):
    """
    Given a list of numbers and a target number, return a list of all combinations
    of the numbers that sum to the target.
    """

    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(numbers)):
            if numbers[i] > target:
                break
            backtrack(i + 1, target - numbers[i], path + [numbers[i]])

    result = []
    numbers.sort()
    backtrack(0, target, [])
    return result


# Set up the Streamlit app
st.title("查找数字加和组合")

# Get the input from the user
numbers = st.text_input("输入一组数字，用逗号','或者换行符'\t'分隔")
target = st.number_input("输入目标数字", format="%0.5f")

click = st.columns([2, 1, 2])[1].button('计算')
if click:
    # Convert the input into a list of integers
    numbers = [float(n.strip()) for n in numbers.replace('，', ' ').replace(',', ' ').replace('\t', ' ').replace('"', '').replace("'", '').split()]

    # Find the combinations that sum to the target
    combinations = find_combinations_summing_to_target(numbers, target)

    # Display the results
    if combinations:
        st.divider()
        st.write(f"共找到 {len(combinations)} 种计算组合的和是 {target}:")
        with st.container():
            for c in combinations:
                st.success(f"{'+'.join(map(str, c))} = {target}")
    else:
        st.write("没有找到可以生成的组合")
