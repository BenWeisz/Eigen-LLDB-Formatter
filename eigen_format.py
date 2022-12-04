# Formatters for some Eigen types

# Base formatter for Eigen Vectors
def _vec_formatter(data):
    return f"Size: {len(data)}\n(" + ", ".join([f"{x:.3f}" for x in data]) + ").T"


def vec3f(valobj, internal_dict, options):
    data = valobj.children[0]
    m_storage = data.children[0]
    m_data = m_storage.children[0]
    array = m_data.children[0]
    floats = array.GetData().floats
    return _vec_formatter(floats)


def vecxf(valobj, internal_dict, options):
    data = valobj.children[0]
    m_storage = data.children[0]
    m_data = m_storage.children[0]
    rows = int(m_storage.GetChildMemberWithName("m_rows").GetValue())

    data_array = m_data.GetPointeeData(0, rows)
    floats = data_array.floats

    return _vec_formatter(floats)


# Base formatter for Eigen Matrices
def _mat_formatter(data, rows, cols):
    format_str = f"Size: {rows} x {cols}\n"
    for y in range(rows):
        format_str += "|"
        for x in range(cols):
            pos = (y * cols) + x
            if str(data[pos])[0] != "-":
                format_str += " "
            format_str += f" {data[pos]:.3f}"
        format_str += " |\n"

    return format_str[: len(format_str) - 1]


# Reinterpret Matrix Data
def _mat_reinterpret(data, rows, cols):
    transposed_data = [0] * len(data)
    for y in range(rows):
        for x in range(cols):
            new_pos = (y * cols) + x
            old_pos = (x * rows) + y

            transposed_data[old_pos] = data[new_pos]

    return transposed_data


def mat2f(valobj, internal_dict, options):
    data = valobj.children[0]
    m_storage = data.children[0]
    m_data = m_storage.children[0]
    array = m_data.children[0]
    floats = array.GetData().floats

    floats = _mat_reinterpret(floats, 2, 2)

    return _mat_formatter(floats, 2, 2)


def mat3f(valobj, internal_dict, options):
    data = valobj.children[0]
    m_storage = data.children[0]
    m_data = m_storage.children[0]
    array = m_data.children[0]
    floats = array.GetData().floats

    floats = _mat_reinterpret(floats, 3, 3)

    return _mat_formatter(floats, 3, 3)


def matxf(valobj, internal_dict, options):
    data = valobj.children[0]
    m_storage = data.children[0]
    m_data = m_storage.children[0]
    rows = int(m_storage.GetChildMemberWithName("m_rows").GetValue())
    cols = int(m_storage.GetChildMemberWithName("m_cols").GetValue())

    data_array = m_data.GetPointeeData(0, rows * cols)
    floats = data_array.floats

    floats = _mat_reinterpret(floats, rows, cols)

    return _mat_formatter(floats, rows, cols)

