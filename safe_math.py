def safe_divide(a, b, default=None):
    try:
        result = a / b
        return result
    except (ZeroDivisionError, TypeError):
        return default
    except Exception:
        return default

assert safe_divide(10, 2) == 5.0
assert safe_divide(10, 0) is None
assert safe_divide("10", 2, default="lỗi kiểu dữ liệu") == "lỗi kiểu dữ liệu"
assert safe_divide(10, "2", default=-1) == -1