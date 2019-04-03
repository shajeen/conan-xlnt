#include <xlnt/xlnt.hpp>
#include <iostream>

int main()
{
    xlnt::workbook wb;
    xlnt::worksheet ws = wb.active_sheet();

    ws.cell("A1").value(5);
    ws.cell("B2").value("string data");
    ws.cell("C3").formula("=RAND()");

    ws.merge_cells("C3:C4");
    ws.freeze_panes("B2");

    wb.save("sample.xlsx");
    std::cout << "Test PASSED \n" ;
    return 0;
}
