import vtkCleanPolyData from '@kitware/vtk.js/Filters/Core/CleanPolyData';
import vtkFillHolesFilter from '@kitware/vtk.js/Filters/Modeling/FillHolesFilter';
import vtkSTLWriter from '@kitware/vtk.js/IO/Geometry/STLWriter';
import vtkSTLReader from '@kitware/vtk.js/IO/Geometry/STLReader';

export async function decimate_mesh(stl_file, { factor }) {
    const vtk = await window.vtkWASM.createNamespace("https://gitlab.kitware.com/api/v4/projects/13/packages/generic/vtk-wasm32-emscripten/9.6.20260228/vtk-9.6.20260228-wasm32-emscripten.tar.gz")
    console.log("decimating with factor, ", factor);

    // TODO: not exposed yet in VTK.wasm :(
    // const stl_reader = vtk.vtkSTLReader()
    const decimate_pro = vtk.vtkDecimatePro();

    return {
        status: true,
        outputs: [
            stl_file
        ]
    }
}

export async function fill_stl_holes(stl_file) {
    const reader = vtkSTLReader.newInstance({
        removeDuplicateVertices: true,
        merging: true,
    });
    const array_buffer = await stl_file.arrayBuffer();    
    reader.parseAsArrayBuffer(array_buffer);

    const cleaner = vtkCleanPolyData.newInstance();
    cleaner.setInputConnection(reader.getOutputPort());
    
    const fill_holes_filters = vtkFillHolesFilter.newInstance();
    fill_holes_filters.setHoleSize(1000.0);
    fill_holes_filters.setInputConnection(cleaner.getOutputPort());

    const stl_content = vtkSTLWriter.writeSTL(fill_holes_filters.getOutputData()); 
    
    return {
        status: true,
        outputs: [
            new File([stl_content], { 
                type: 'model/stl'
            })
        ]
    }
}
