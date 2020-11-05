<?php 
public function bm_export_media(){
        $result = $this->db->select("m.`title`,replace(med.`file_url`,'http://chaptervitaminsnew.s3.amazonaws.com','http://local.chaptervitamins.com') as file_url,med.`modified_on`")
            ->from(MEDIA_TABLE.' as med')
            ->join(MATERIAL_TABLE.' as m','m.material_media_id=med.media_id')
            ->join(MODULE_TABLE.' as md','md.module_id=m.module_id')
            ->join(COURSE_TABLE.' as c','c.course_id=md.course_id')
            ->where(['c.`branch_id`' => 50, 'c.`is_deleted`'=>0,'c.`is_inactive`'=>0,'m.`is_deleted`'=>0,'m.`is_inactive`'=>0,'md.`is_deleted`'=>0,'md.`is_inactive`'=>0,'med.`is_deleted`'=>0,'med.`is_inactive`'=>0])
            ->where("m.`material_type` != 'tincan-scrom' and m.`material_type` != 'link' and m.`material_type` != 'IFRAME'")
            ->get()
            ->result_array();

        $this->load->library('excel');

        if($result) {
            foreach ($result as $key => $u) {
                $x = 'A';
                foreach (array_values((array)$u) as $value) {
                    if ($value == 'HOLD') {
                        $value = 'On Hold';
                    }
                    $this->excel->getActiveSheet()->setCellValue($x . ($key + 1), $value);
                    $x++;
                }
            }
        }

        $filename = 'bharat_matrimony_videos.csv';



        header('Content-Type: text/csv; charset=utf-8');

        header('Content-Disposition: attachment;filename="' . $filename . '"');

        header('Cache-Control: max-age=0');

        $objWriter = PHPExcel_IOFactory::createWriter($this->excel, 'CSV');
        ob_end_clean();
        $objWriter->save('php://output');

        exit;
    }





#Or another static approach

$this->load->library('excel');
            $objPHPExcel = $this->excel;
            $objPHPExcel->createSheet();
            $objPHPExcel->setActiveSheetIndex(0)->setTitle("Material Details");
            $objPHPExcel->getActiveSheet()->setCellValue('A1',"Title");
            $objPHPExcel->getActiveSheet()->setCellValue('B1',"Material Type");
            $objPHPExcel->getActiveSheet()->setCellValue('C1',"Material URL");
            $objPHPExcel->getActiveSheet()->setCellValue('D1',"Added On");
            $objPHPExcel->getActiveSheet()->setCellValue('E1',"Last Modified On");
            $i=2;
        if($responses) {
            foreach ($responses as $response) {
                // echo "<pre>";print_r($response);die;
               $objPHPExcel->getActiveSheet()->setCellValue('A'.$i,$response['title']);
               $objPHPExcel->getActiveSheet()->setCellValue('B'.$i,$response['material_type']);
               $objPHPExcel->getActiveSheet()->setCellValue('C'.$i,$response['file_url']);
               $objPHPExcel->getActiveSheet()->setCellValue('D'.$i,$response['added_on']);
               $objPHPExcel->getActiveSheet()->setCellValue('E'.$i,$response['modified_on']);
                $i++;
            }
        }
        $filename = 'materialDataDetails.csv';



        header('Content-Type: text/csv; charset=utf-8');

        header('Content-Disposition: attachment;filename="' . $filename . '"');

        header('Cache-Control: max-age=0');

        $objWriter = PHPExcel_IOFactory::createWriter($this->excel, 'CSV');
        ob_end_clean();
        $objWriter->save('php://output');
?>
